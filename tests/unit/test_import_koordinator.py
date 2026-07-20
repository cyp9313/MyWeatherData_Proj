"""Tests für `LufttemperaturImportKoordinator` (FR-001, FR-005, FR-006)."""

from __future__ import annotations

from datetime import date
from unittest.mock import Mock

from myweatherdata.domain.import_ergebnis import ImportErgebnis
from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.domain.stationstreffer import StationsTreffer
from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.import_koordinator import LufttemperaturImportKoordinator


def test_ergebnis_station_entspricht_treffer_des_stationsfinder_unveraendert() -> None:
    station = StationsTreffer(station_id="00019", name="Teststation Nord", entfernung_km=12.3)
    stationsfinder = Mock()
    stationsfinder.finde_naechste.return_value = station

    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))
    importer_ergebnis = ImportErgebnis(
        station=StationsTreffer(station_id="00019", name="", entfernung_km=0.0),
        messwerte=[],
        verwendeter_zeitraum=zeitraum,
        hinweise=[],
    )
    importer = Mock()
    importer.importiere.return_value = importer_ergebnis

    koordinator = LufttemperaturImportKoordinator(stationsfinder, importer)

    ergebnis = koordinator.importiere_lufttemperatur(
        Koordinate(breitengrad=50.0, laengengrad=10.0), zeitraum
    )

    assert ergebnis.station == station
    importer.importiere.assert_called_once_with("00019", zeitraum)


def test_verwendeter_zeitraum_entspricht_dem_vom_importer_gekuerzten_zeitraum() -> None:
    station = StationsTreffer(station_id="00019", name="Teststation Nord", entfernung_km=12.3)
    stationsfinder = Mock()
    stationsfinder.finde_naechste.return_value = station

    angefragter_zeitraum = Zeitraum(start=date(2014, 6, 1), ende=date(2020, 1, 1))
    gekuerzter_zeitraum = Zeitraum(start=date(2015, 1, 1), ende=date(2020, 1, 1))
    importer_ergebnis = ImportErgebnis(
        station=StationsTreffer(station_id="00019", name="", entfernung_km=0.0),
        messwerte=[],
        verwendeter_zeitraum=gekuerzter_zeitraum,
        hinweise=["Der angefragte Zeitraum wurde gekürzt."],
    )
    importer = Mock()
    importer.importiere.return_value = importer_ergebnis

    koordinator = LufttemperaturImportKoordinator(stationsfinder, importer)

    ergebnis = koordinator.importiere_lufttemperatur(
        Koordinate(breitengrad=50.0, laengengrad=10.0), angefragter_zeitraum
    )

    assert ergebnis.verwendeter_zeitraum == gekuerzter_zeitraum
