"""End-to-End-Test des Lufttemperatur-Imports (FR-001, FR-004, FR-005, FR-006, FR-007, FR-008).

Verwendet ausschließlich lokale Fixture-Bytes über `FakeHttpClient` -
kein Zugriff auf das echte DWD-Netzwerk.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.import_koordinator import LufttemperaturImportKoordinator
from myweatherdata.import_client.lufttemperatur_importer import (
    HISTORICAL_VERZEICHNIS_URL,
    LufttemperaturImporter,
)
from myweatherdata.import_client.stationsfinder import STATIONSLISTE_URL, StationsFinder
from tests.conftest import FakeHttpClient

_FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "dwd"
_AACHEN_STATION_ID = "00003"
_AACHEN_ZIP_DATEINAME = f"10minutenwerte_TU_{_AACHEN_STATION_ID}_20150101_20251231_hist.zip"


def _koordinator_mit_fixtures() -> LufttemperaturImportKoordinator:
    stationsliste_bytes = (_FIXTURES / "stationsliste_beispiel.txt").read_bytes()
    zip_bytes = (_FIXTURES / "10minutenwerte_TU_00003_beispiel_hist.zip").read_bytes()
    listing_bytes = f'<a href="{_AACHEN_ZIP_DATEINAME}">...</a>'.encode("latin-1")

    http_client = FakeHttpClient(
        {
            STATIONSLISTE_URL: stationsliste_bytes,
            HISTORICAL_VERZEICHNIS_URL: listing_bytes,
            HISTORICAL_VERZEICHNIS_URL + _AACHEN_ZIP_DATEINAME: zip_bytes,
        }
    )
    stationsfinder = StationsFinder(http_client)
    importer = LufttemperaturImporter(http_client)
    return LufttemperaturImportKoordinator(stationsfinder, importer)


def test_import_lufttemperatur_end_to_end_liefert_vollstaendiges_ergebnis() -> None:
    koordinator = _koordinator_mit_fixtures()
    koordinate_nahe_aachen = Koordinate(breitengrad=50.78, laengengrad=6.09)
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    ergebnis = koordinator.importiere_lufttemperatur(koordinate_nahe_aachen, zeitraum)

    assert ergebnis.station.station_id == _AACHEN_STATION_ID
    assert ergebnis.station.name == "Aachen"
    assert len(ergebnis.messwerte) == 5
    assert ergebnis.verwendeter_zeitraum == zeitraum
    assert ergebnis.hinweise == []
