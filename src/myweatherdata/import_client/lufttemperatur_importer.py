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
from myweatherdata.import_client.dwd_zip_reader import lese_rohdatensaetze
from myweatherdata.ports.http_client_port import HttpClient

ZIP_URL_TEMPLATE = (
    "https://opendata.dwd.de/climate_environment/CDC/observations_germany/"
    "climate/10_minutes/air_temperature/historical/"
    "10minutenwerte_TU_{station_id}_hist.zip"
)
"""URL-Vorlage für die stationsbezogene DWD-Messdaten-ZIP (Spike-Annahme,
siehe arc/statische_sichten/klassensicht.md, Weitere Confirmation-Punkte Nr. 4;
vereinfacht ohne den realen Datumsbereich im Dateinamen, noch nicht gegen
einen Live-Abruf verifiziert)."""

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

        zip_bytes = self._http_client.get_bytes(ZIP_URL_TEMPLATE.format(station_id=station_id))
        rohdatensaetze = lese_rohdatensaetze(zip_bytes)

        messwerte = self._zu_messwerten(rohdatensaetze, verwendeter_zeitraum)

        if not messwerte:
            hinweise.append(_HINWEIS_DATENLUECKE)

        return ImportErgebnis(
            station=StationsTreffer(station_id=station_id, name="", entfernung_km=0.0),
            messwerte=messwerte,
            verwendeter_zeitraum=verwendeter_zeitraum,
            hinweise=hinweise,
        )

    def _zu_messwerten(
        self, rohdatensaetze: list[dict[str, str]], zeitraum: Zeitraum
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
                    station_id=rohdatensatz["STATIONS_ID"],
                    zeitstempel=zeitstempel,
                    messgroesse=Messgroesse.LUFTTEMPERATUR,
                    wert=float(rohdatensatz["TT_10"]),
                )
            )
        return messwerte
