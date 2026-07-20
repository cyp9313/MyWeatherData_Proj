"""Wertobjekt für das Ergebnis der Stationssuche."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StationsTreffer:
    """Ergebnis der Stationssuche: nächstgelegene Station mit Entfernung (FR-001, FR-004)."""

    station_id: str
    name: str
    entfernung_km: float
