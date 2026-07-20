"""Wertobjekt für eine geografische Koordinate (Breiten-/Längengrad)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Koordinate:
    """Geografische Koordinate einer Nutzereingabe (FR-001)."""

    breitengrad: float
    laengengrad: float
