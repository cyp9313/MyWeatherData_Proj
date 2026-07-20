"""Domänentypen für Messgrößen und einzelne Messwerte.

`Messgroesse` umfasst in diesem Vertical Slice bewusst nur `LUFTTEMPERATUR`
(FR-005); weitere Messgrößen (Niederschlag, Wind, Sonneneinstrahlung) sind
zurückgestellt (siehe pjm/vertical-slice-prototyp.md). Der gemeinsame
Ablageort von `Messgroesse`/`Messwert` über Import-Client und Datenhaltung
hinweg ist mit dem Datenhaltung-Verantwortlichen noch abzustimmen (siehe
arc/statische_sichten/klassensicht.md, Weitere Confirmation-Punkte).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class Messgroesse(Enum):
    """Unterstützte Messgrößen. In diesem Vertical Slice nur `LUFTTEMPERATUR`."""

    LUFTTEMPERATUR = auto()


@dataclass(frozen=True)
class Messwert:
    """Einzelner Messwert einer Station zu einem Zeitpunkt/einer Messgröße."""

    station_id: str
    zeitstempel: datetime
    messgroesse: Messgroesse
    wert: float
