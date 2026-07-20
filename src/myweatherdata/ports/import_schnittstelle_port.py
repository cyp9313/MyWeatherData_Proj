"""Core/Application-eigener Port für den Import von Wetterdaten.

Dieses Protocol gehört konzeptionell dem Core/der Application-Schicht (siehe
arc/statische_sichten/klassensicht-core.puml). Es liegt aus Scope-Gründen
(YAGNI, noch kein eigenes Core-Package im aktuellen Vertical Slice) unter
`ports/`, wird aber vom Import-Client (`LufttemperaturImportKoordinator`,
siehe import_client/import_koordinator.py) realisiert, nicht besessen.
"""

from __future__ import annotations

from typing import Protocol

from myweatherdata.domain.import_ergebnis import ImportErgebnis
from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.domain.zeitraum import Zeitraum


class ImportSchnittstelle(Protocol):
    """Core-eigener Port zum Anstoßen eines Lufttemperatur-Imports."""

    def importiere_lufttemperatur(
        self, koordinate: Koordinate, zeitraum: Zeitraum
    ) -> ImportErgebnis:
        """Importiert Lufttemperaturdaten für die nächstgelegene Station (FR-001, FR-005)."""
        ...
