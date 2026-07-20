"""Wertobjekt für einen Zeitraum beim Import von Wetterdaten."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

_UNTERSTUETZTER_BEREICH_START = date(2015, 1, 1)
_UNTERSTUETZTER_BEREICH_ENDE = date(2025, 12, 31)


@dataclass(frozen=True)
class Zeitraum:
    """Zeitraum für einen Datenimport, begrenzt durch Start- und Enddatum (inklusive)."""

    start: date
    ende: date

    def __post_init__(self) -> None:
        if self.start > self.ende:
            raise ValueError("Zeitraum.start darf nicht nach Zeitraum.ende liegen.")

    def liegt_vollstaendig_im_unterstuetzten_bereich(self) -> bool:
        """Prüft, ob der Zeitraum vollständig innerhalb 01.01.2015–31.12.2025 liegt (FR-005)."""
        return (
            self.start >= _UNTERSTUETZTER_BEREICH_START
            and self.ende <= _UNTERSTUETZTER_BEREICH_ENDE
        )

    def hat_ueberschneidung_mit_unterstuetztem_bereich(self) -> bool:
        """Prüft, ob sich der Zeitraum mit 01.01.2015–31.12.2025 überhaupt überschneidet (FR-006).

        Liefert `False`, wenn der Zeitraum vollständig VOR oder vollständig NACH dem
        unterstützten Bereich liegt; in diesem Fall ist `gekuerzt_auf_unterstuetzten_bereich()`
        NICHT aufrufbar (kein gültiger, nicht-leerer geschnittener Zeitraum existiert).
        """
        return (
            self.start <= _UNTERSTUETZTER_BEREICH_ENDE
            and self.ende >= _UNTERSTUETZTER_BEREICH_START
        )

    def gekuerzt_auf_unterstuetzten_bereich(self) -> Zeitraum:
        """Kürzt den Zeitraum auf den unterstützten Bereich 01.01.2015–31.12.2025 (FR-006)."""
        neuer_start = max(self.start, _UNTERSTUETZTER_BEREICH_START)
        neues_ende = min(self.ende, _UNTERSTUETZTER_BEREICH_ENDE)
        return Zeitraum(start=neuer_start, ende=neues_ende)
