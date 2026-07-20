"""Import der 10-Minuten-Lufttemperaturwerte einer Station für einen Zeitraum.

Deckt FR-005 (Import gültiger Zeitraum), FR-006 (Kürzung außerhalb des
unterstützten Bereichs), FR-007 (fehlerhafte/unvollständige Datensätze) und
FR-008 (Datenlücke/leeres Ergebnis) ab.
"""

from __future__ import annotations

from datetime import datetime

from myweatherdata.domain.import_ergebnis import ImportErgebnis
from myweatherdata.domain.messwert import Messgroesse, Messwert
from myweatherdata.domain.stationstreffer import StationsTreffer
from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.datensatz_validator import DatensatzValidator
from myweatherdata.import_client.dwd_archiv_verzeichnis import (
    passende_zip_dateinamen,
    zip_dateinamen_aus_listing,
)
from myweatherdata.import_client.dwd_zip_reader import lese_rohdatensaetze
from myweatherdata.ports.http_client_port import HttpClient

HISTORICAL_VERZEICHNIS_URL = (
    "https://opendata.dwd.de/climate_environment/CDC/observations_germany/"
    "climate/10_minutes/air_temperature/historical/"
)
"""Verzeichnis-URL des historischen 10-Minuten-Lufttemperatur-Archivs. Gegen einen
echten Live-Abruf verifiziert (Real-DWD Contract Spike, Phase 5.5, siehe
`doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 2). Das passende ZIP für eine
Station und einen Zeitraum wird über `dwd_archiv_verzeichnis` ermittelt, da reale
ZIP-Dateinamen stets einen Datumsbereich enthalten und pro Station mehrere,
nicht überlappende ZIP-Dateien existieren können (siehe Design-Entscheidung
Phase 7R in `pjm/import-client-implementation-plan.md`)."""

_ZEITSTEMPEL_FORMAT = "%Y%m%d%H%M"
_HINWEIS_KUERZUNG = (
    "Der angefragte Zeitraum wurde auf den unterstützten Bereich 01.01.2015-31.12.2025 gekürzt."
)
_HINWEIS_DATENLUECKE = (
    "Für den angefragten Zeitraum liegen keine Messwerte der Station vor (Datenlücke)."
)


class LufttemperaturImporter:
    """Importiert 10-Minuten-Lufttemperaturwerte einer Station für einen Zeitraum.

    `ImportErgebnis.station` wird hier nur mit einem Platzhalter (Stations-ID,
    keine weiteren Stationsdaten) befüllt; die vollständige `StationsTreffer`
    wird erst vom `LufttemperaturImportKoordinator` ergänzt.
    """

    def __init__(
        self, http_client: HttpClient, validator: DatensatzValidator | None = None
    ) -> None:
        self._http_client = http_client
        self._validator = validator or DatensatzValidator()

    def importiere(self, station_id: str, zeitraum: Zeitraum) -> ImportErgebnis:
        """Importiert Lufttemperaturdaten der Station für den angegebenen Zeitraum."""
        hinweise: list[str] = []
        verwendeter_zeitraum = zeitraum
        if not zeitraum.liegt_vollstaendig_im_unterstuetzten_bereich():
            if not zeitraum.hat_ueberschneidung_mit_unterstuetztem_bereich():
                return ImportErgebnis(
                    station=StationsTreffer(station_id=station_id, name="", entfernung_km=0.0),
                    messwerte=[],
                    verwendeter_zeitraum=zeitraum,
                    hinweise=[_HINWEIS_DATENLUECKE],
                )
            verwendeter_zeitraum = zeitraum.gekuerzt_auf_unterstuetzten_bereich()
            hinweise.append(_HINWEIS_KUERZUNG)

        listing_html = self._http_client.get_bytes(HISTORICAL_VERZEICHNIS_URL).decode("latin-1")
        dateinamen = zip_dateinamen_aus_listing(listing_html, station_id)
        passende_dateinamen = passende_zip_dateinamen(dateinamen, verwendeter_zeitraum)

        rohdatensaetze: list[dict[str, str]] = []
        for dateiname in passende_dateinamen:
            zip_bytes = self._http_client.get_bytes(HISTORICAL_VERZEICHNIS_URL + dateiname)
            rohdatensaetze.extend(lese_rohdatensaetze(zip_bytes))

        messwerte = self._zu_messwerten(station_id, rohdatensaetze, verwendeter_zeitraum)

        if not messwerte:
            hinweise.append(_HINWEIS_DATENLUECKE)

        return ImportErgebnis(
            station=StationsTreffer(station_id=station_id, name="", entfernung_km=0.0),
            messwerte=messwerte,
            verwendeter_zeitraum=verwendeter_zeitraum,
            hinweise=hinweise,
        )

    def _zu_messwerten(
        self, station_id: str, rohdatensaetze: list[dict[str, str]], zeitraum: Zeitraum
    ) -> list[Messwert]:
        messwerte: list[Messwert] = []
        for rohdatensatz in rohdatensaetze:
            if not self._validator.validiere(rohdatensatz):
                continue
            zeitstempel = datetime.strptime(rohdatensatz["MESS_DATUM"], _ZEITSTEMPEL_FORMAT)
            if not (zeitraum.start <= zeitstempel.date() <= zeitraum.ende):
                continue
            messwerte.append(
                Messwert(
                    # Die angefragte station_id (nicht das rohe CSV-Feld) wird verwendet,
                    # da die reale STATIONS_ID-Spalte rechtsbündig ohne führende Nullen
                    # vorliegt (Contract Baseline Abschnitt 2) und sonst inkonsistent zu
                    # ImportErgebnis.station.station_id wäre (DQA-5).
                    station_id=station_id,
                    zeitstempel=zeitstempel,
                    messgroesse=Messgroesse.LUFTTEMPERATUR,
                    wert=float(rohdatensatz["TT_10"]),
                )
            )
        return messwerte
