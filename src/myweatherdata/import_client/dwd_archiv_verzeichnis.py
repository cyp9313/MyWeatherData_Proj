"""Ermittelt passende DWD-ZIP-Dateinamen über das reale Verzeichnis-Listing (FR-005/006).

Siehe Design-Entscheidung in `pjm/import-client-implementation-plan.md`, Abschnitt
"Design-Entscheidung Phase 7R — ZIP-Ermittlung über Verzeichnis-Listing", und die
verifizierte Kontrakt-Baseline `doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 2.
"""

from __future__ import annotations

import re
from datetime import date, datetime

from myweatherdata.domain.zeitraum import Zeitraum

_DATEINAME_ZEITSTEMPEL_FORMAT = "%Y%m%d"
_DATUMSBEREICH_MUSTER = re.compile(r"_(\d{8})_(\d{8})_hist\.zip$")


def zip_dateinamen_aus_listing(listing_html: str, station_id: str) -> list[str]:
    """Extrahiert alle ZIP-Dateinamen der gegebenen Station aus dem HTML-Verzeichnis-Listing."""
    muster = rf'href="(10minutenwerte_TU_{re.escape(station_id)}_[^"]+\.zip)"'
    return re.findall(muster, listing_html)


def passende_zip_dateinamen(dateinamen: list[str], zeitraum: Zeitraum) -> list[str]:
    """Wählt die Dateinamen aus, deren im Namen kodierter Datumsbereich sich mit
    dem angefragten Zeitraum überschneidet."""
    passende: list[str] = []
    for dateiname in dateinamen:
        bereich = _datumsbereich_aus_dateiname(dateiname)
        if bereich is None:
            continue
        begin, ende = bereich
        if begin <= zeitraum.ende and ende >= zeitraum.start:
            passende.append(dateiname)
    return passende


def _datumsbereich_aus_dateiname(dateiname: str) -> tuple[date, date] | None:
    treffer = _DATUMSBEREICH_MUSTER.search(dateiname)
    if treffer is None:
        return None
    try:
        begin = datetime.strptime(treffer.group(1), _DATEINAME_ZEITSTEMPEL_FORMAT).date()
        ende = datetime.strptime(treffer.group(2), _DATEINAME_ZEITSTEMPEL_FORMAT).date()
    except ValueError:
        return None
    return begin, ende
