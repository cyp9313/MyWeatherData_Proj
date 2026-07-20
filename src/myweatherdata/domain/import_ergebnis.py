"""Wertobjekt für das Ergebnis eines Lufttemperatur-Importvorgangs."""

from __future__ import annotations

from dataclasses import dataclass, field

from myweatherdata.domain.messwert import Messwert
from myweatherdata.domain.stationstreffer import StationsTreffer
from myweatherdata.domain.zeitraum import Zeitraum


@dataclass(frozen=True)
class ImportErgebnis:
    """Ergebnis eines Importvorgangs: Station, Messwerte, verwendeter Zeitraum, Hinweise."""

    station: StationsTreffer
    messwerte: list[Messwert]
    verwendeter_zeitraum: Zeitraum
    hinweise: list[str] = field(default_factory=list)
