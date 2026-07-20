"""Tests für `parse_stationsliste()` gegen reale DWD-Kontraktdaten (Phase 6R).

Ergänzt `tests/unit/test_stationsfinder.py` (synthetische Fixture, FR-001/FR-004)
um einen direkten Parser-Test mit einem realen, reduzierten Auszug aus der
live abgerufenen DWD-Stationsliste (siehe `doc/DWD/dwd-import-contract-baseline.md`,
Abschnitt 1, und `tests/fixtures/dwd/README.md`).
"""

from __future__ import annotations

from pathlib import Path

from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.import_client.dwd_stationsliste_parser import (
    StationsListenEintrag,
    parse_stationsliste,
)

_FIXTURE_PFAD = (
    Path(__file__).resolve().parents[1] / "fixtures" / "dwd" / "stationsliste_real_auszug.txt"
)


def _real_auszug() -> str:
    return _FIXTURE_PFAD.read_text(encoding="latin-1")


def test_realer_auszug_liefert_alle_sechs_datenzeilen_als_eintraege() -> None:
    eintraege = parse_stationsliste(_real_auszug())

    assert len(eintraege) == 6


def test_realer_auszug_station_00003_wird_korrekt_geparst() -> None:
    eintraege = parse_stationsliste(_real_auszug())

    aachen = next(e for e in eintraege if e.station_id == "00003")

    assert aachen == StationsListenEintrag(
        station_id="00003",
        name="Aachen",
        koordinate=Koordinate(breitengrad=50.7827, laengengrad=6.0941),
    )


def test_realer_auszug_mit_vierstelliger_stationshoehe_wird_korrekt_geparst() -> None:
    """Station 20098 (Seebach) hat eine 4-stellige Stationshöhe (1019 m) - Regressionstest
    für den festen Byte-Offset-Parser gegen wechselnde Ziffernlängen."""
    eintraege = parse_stationsliste(_real_auszug())

    seebach = next(e for e in eintraege if e.station_id == "20098")

    assert seebach.koordinate == Koordinate(breitengrad=48.5651, laengengrad=8.2284)
