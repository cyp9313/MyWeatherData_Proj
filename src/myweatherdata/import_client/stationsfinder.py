"""Ermittelt die nächstgelegene DWD-Station zu einer Koordinate (FR-001, FR-004)."""

from __future__ import annotations

from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.domain.stationstreffer import StationsTreffer
from myweatherdata.import_client.distanz import distanz_km
from myweatherdata.import_client.dwd_stationsliste_parser import (
    StationsListenEintrag,
    parse_stationsliste,
)
from myweatherdata.ports.http_client_port import HttpClient

STATIONSLISTE_URL = (
    "https://opendata.dwd.de/climate_environment/CDC/observations_germany/"
    "climate/10_minutes/air_temperature/historical/"
    "zehn_min_tu_Beschreibung_Stationen.txt"
)
"""URL des DWD-`help`-Verzeichnisses mit der Stationsliste (Spike-Annahme,
siehe arc/statische_sichten/klassensicht.md, Weitere Confirmation-Punkte Nr. 4;
noch nicht gegen einen Live-Abruf verifiziert)."""


class StationsFinder:
    """Ermittelt zu einer Koordinate die nächstgelegene DWD-Station (FR-001, FR-004)."""

    def __init__(self, http_client: HttpClient) -> None:
        self._http_client = http_client

    def finde_naechste(self, koordinate: Koordinate) -> StationsTreffer:
        """Liefert die Station mit der geringsten Entfernung zur Koordinate.

        Bei mehreren Stationen mit identischer minimaler Entfernung wird die
        Station mit der (numerisch) niedrigsten Stations-ID gewählt (FR-004);
        die Ausgabe behält die ursprüngliche String-Repräsentation der
        Stations-ID (inkl. führender Nullen) bei.
        """
        inhalt = self._http_client.get_bytes(STATIONSLISTE_URL).decode("latin-1")
        eintraege = parse_stationsliste(inhalt)
        if not eintraege:
            raise ValueError("Stationsliste ist leer.")

        kandidaten = [
            (distanz_km(koordinate, eintrag.koordinate), eintrag) for eintrag in eintraege
        ]
        minimale_distanz = min(distanz for distanz, _ in kandidaten)
        gleichstand: list[StationsListenEintrag] = [
            eintrag for distanz, eintrag in kandidaten if distanz == minimale_distanz
        ]
        gewinner = min(gleichstand, key=lambda eintrag: int(eintrag.station_id))

        return StationsTreffer(
            station_id=gewinner.station_id,
            name=gewinner.name,
            entfernung_km=minimale_distanz,
        )
