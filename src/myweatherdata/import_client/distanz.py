"""Distanzberechnung zwischen zwei Koordinaten mittels Haversine-Formel (FR-001)."""

from __future__ import annotations

from math import asin, cos, radians, sin, sqrt

from myweatherdata.domain.koordinate import Koordinate

_ERDRADIUS_KM = 6371.0


def distanz_km(punkt_a: Koordinate, punkt_b: Koordinate) -> float:
    """Berechnet die Großkreisentfernung zwischen zwei Koordinaten in km."""
    lat1, lon1 = radians(punkt_a.breitengrad), radians(punkt_a.laengengrad)
    lat2, lon2 = radians(punkt_b.breitengrad), radians(punkt_b.laengengrad)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return _ERDRADIUS_KM * c
