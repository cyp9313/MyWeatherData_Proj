"""Fassade des Import-Client: realisiert den Core-eigenen Port `ImportSchnittstelle`.

`LufttemperaturImportKoordinator` orchestriert NUR den internen Ablauf
`StationsFinder` -> `LufttemperaturImporter` dieses Adapters, nicht den
Core-weiten Ablauf (siehe `DatenabrufKoordinator` in
arc/statische_sichten/klassensicht-core.puml).
"""

from __future__ import annotations

from dataclasses import replace

from myweatherdata.domain.import_ergebnis import ImportErgebnis
from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.lufttemperatur_importer import LufttemperaturImporter
from myweatherdata.import_client.stationsfinder import StationsFinder


class LufttemperaturImportKoordinator:
    """Realisiert `ImportSchnittstelle` (FR-001, FR-005)."""

    def __init__(self, stationsfinder: StationsFinder, importer: LufttemperaturImporter) -> None:
        self._stationsfinder = stationsfinder
        self._importer = importer

    def importiere_lufttemperatur(
        self, koordinate: Koordinate, zeitraum: Zeitraum
    ) -> ImportErgebnis:
        """Ermittelt die nächstgelegene Station und importiert deren Lufttemperaturdaten."""
        station = self._stationsfinder.finde_naechste(koordinate)
        ergebnis = self._importer.importiere(station.station_id, zeitraum)
        return replace(ergebnis, station=station)
