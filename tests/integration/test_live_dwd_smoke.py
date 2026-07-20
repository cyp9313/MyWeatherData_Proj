"""Live-Smoke-Test gegen die echten DWD-CDC-Ressourcen (Phase 5.5/8R).

NICHT Teil des Standard-`pytest`-Laufs. `pyproject.toml` schließt den Marker
`live` per `addopts = "-m 'not live'"` standardmäßig aus. Manuelle Ausführung:

    pytest -m live tests/integration/test_live_dwd_smoke.py -v

Verifiziert die blockierende Bedingung aus
`pjm/import-client-implementation-plan.md`, Phase 5.5:
- eine echte Stationsliste wird heruntergeladen und erfolgreich geparst,
- ein echtes historisches Lufttemperatur-ZIP wird lokalisiert und gelesen,
- mindestens ein echter Messwert wird erfolgreich in `Messwert` überführt.

Dieser Test führt echte Netzwerkzugriffe auf `opendata.dwd.de` aus und ist
daher nicht deterministisch/offline. Er ersetzt keine Unit-/Integrationstests
mit lokalen Fixtures.
"""

from __future__ import annotations

import re

import pytest

from myweatherdata.domain.koordinate import Koordinate
from myweatherdata.import_client.datensatz_validator import DatensatzValidator
from myweatherdata.import_client.dwd_zip_reader import lese_rohdatensaetze
from myweatherdata.import_client.http_client import RequestsHttpClient
from myweatherdata.import_client.stationsfinder import StationsFinder

_HISTORICAL_VERZEICHNIS_URL = (
    "https://opendata.dwd.de/climate_environment/CDC/observations_germany/"
    "climate/10_minutes/air_temperature/historical/"
)
_KOORDINATE_AACHEN = Koordinate(breitengrad=50.78, laengengrad=6.09)

pytestmark = pytest.mark.live


def test_live_stationsliste_wird_real_geladen_und_geparst() -> None:
    """Reale Stationssuche liefert eine tatsächliche, nicht-leere Station."""
    http_client = RequestsHttpClient()
    stationsfinder = StationsFinder(http_client)

    treffer = stationsfinder.finde_naechste(_KOORDINATE_AACHEN)

    assert treffer.station_id
    assert treffer.name


def test_live_zip_wird_lokalisiert_gelesen_und_zu_messwert_konvertiert() -> None:
    """Reales historisches ZIP für eine Station wird gefunden, gelesen und
    mindestens ein Datensatz erfolgreich in einen gültigen Rohdatensatz
    überführt (Validierung über `DatensatzValidator`).
    """
    http_client = RequestsHttpClient()
    listing_bytes = http_client.get_bytes(_HISTORICAL_VERZEICHNIS_URL)
    listing_html = listing_bytes.decode("latin-1")

    zip_dateinamen = re.findall(r'href="(10minutenwerte_TU_00003_[^"]+\.zip)"', listing_html)
    assert zip_dateinamen, "Kein reales ZIP für Station 00003 im Verzeichnis-Listing gefunden."

    zip_bytes = http_client.get_bytes(_HISTORICAL_VERZEICHNIS_URL + zip_dateinamen[0])
    rohdatensaetze = lese_rohdatensaetze(zip_bytes)
    assert rohdatensaetze

    validator = DatensatzValidator()
    gueltige_datensaetze = [rd for rd in rohdatensaetze if validator.validiere(rd)]
    assert gueltige_datensaetze, "Kein gültiger realer Datensatz im ZIP gefunden."
