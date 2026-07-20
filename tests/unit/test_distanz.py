"""Tests für die Distanzberechnung (Haversine) zwischen zwei Koordinaten (FR-001)."""

from __future__ import annotations

from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.import_client.distanz import distanz_km


def test_distanz_zwischen_identischer_koordinate_ist_null() -> None:
    punkt = Koordinate(breitengrad=52.5200, laengengrad=13.4050)

    assert distanz_km(punkt, punkt) == 0.0


def test_distanz_zwischen_bekannten_koordinaten_entspricht_referenzwert() -> None:
    punkt_a = Koordinate(breitengrad=0.0, laengengrad=0.0)
    punkt_b = Koordinate(breitengrad=0.0, laengengrad=1.0)

    ergebnis = distanz_km(punkt_a, punkt_b)

    # 1 Längengrad am Äquator entspricht bei Erdradius 6371 km rund 111,19 km.
    assert abs(ergebnis - 111.19) < 0.1
