"""Tests für `StationsFinder` inkl. DWD-Stationsliste-Parsing (FR-001, FR-004)."""

from __future__ import annotations

from pathlib import Path

import pytest

from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.import_client.stationsfinder import STATIONSLISTE_URL, StationsFinder
from tests.conftest import FakeHttpClient

_FIXTURE_PFAD = (
    Path(__file__).resolve().parents[1] / "fixtures" / "dwd" / "stationsliste_beispiel.txt"
)


def _http_client_mit_fixture() -> FakeHttpClient:
    inhalt = _FIXTURE_PFAD.read_bytes()
    return FakeHttpClient({STATIONSLISTE_URL: inhalt})


def test_eindeutig_naechstgelegene_station_wird_ermittelt() -> None:
    finder = StationsFinder(_http_client_mit_fixture())

    treffer = finder.finde_naechste(Koordinate(breitengrad=48.001, laengengrad=11.0))

    assert treffer.station_id == "00050"
    assert treffer.name == "Teststation Nah"


def test_distanz_gleichstand_waehlt_niedrigere_stations_id() -> None:
    finder = StationsFinder(_http_client_mit_fixture())

    treffer = finder.finde_naechste(Koordinate(breitengrad=50.0, laengengrad=10.0))

    assert treffer.station_id == "00019"


def test_drei_stationen_mit_identischer_distanz_waehlt_niedrigste_id(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        "myweatherdata.import_client.stationsfinder.distanz_km",
        lambda koordinate, ziel: 42.0,
    )
    finder = StationsFinder(_http_client_mit_fixture())

    treffer = finder.finde_naechste(Koordinate(breitengrad=0.0, laengengrad=0.0))

    assert treffer.station_id == "00003"


def test_leere_stationsliste_wirft_value_error() -> None:
    leere_liste = FakeHttpClient({STATIONSLISTE_URL: b"Stations_id\n-----------\n"})
    finder = StationsFinder(leere_liste)

    with pytest.raises(ValueError):
        finder.finde_naechste(Koordinate(breitengrad=50.0, laengengrad=10.0))


# --- Destructive QA: DQA-3 (fehlerhafte/unvollständige Stationszeile darf nicht abstürzen) ---

_FIXTURE_DEFEKTE_ZEILE_PFAD = (
    Path(__file__).resolve().parents[1] / "fixtures" / "dwd" / "stationsliste_defekte_zeile.txt"
)


def test_stationsliste_mit_unvollstaendiger_zeile_wird_ohne_absturz_verarbeitet() -> None:
    """DQA-3: Eine zu kurze/unvollständige Stationszeile darf nicht zum Absturz führen."""
    inhalt = _FIXTURE_DEFEKTE_ZEILE_PFAD.read_bytes()
    finder = StationsFinder(FakeHttpClient({STATIONSLISTE_URL: inhalt}))

    treffer = finder.finde_naechste(Koordinate(breitengrad=48.001, laengengrad=11.0))

    assert treffer.station_id == "00050"
