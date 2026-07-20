"""Tests für `LufttemperaturImporter` (FR-005, FR-006, FR-007, FR-008)."""

from __future__ import annotations

from datetime import date
from pathlib import Path

from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.lufttemperatur_importer import (
    ZIP_URL_TEMPLATE,
    LufttemperaturImporter,
)
from tests.conftest import FakeHttpClient

_FIXTURE_PFAD = (
    Path(__file__).resolve().parents[1]
    / "fixtures"
    / "dwd"
    / "10minutenwerte_TU_00003_beispiel_hist.zip"
)
_STATION_ID = "00003"


def _importer_mit_fixture() -> LufttemperaturImporter:
    zip_bytes = _FIXTURE_PFAD.read_bytes()
    url = ZIP_URL_TEMPLATE.format(station_id=_STATION_ID)
    return LufttemperaturImporter(FakeHttpClient({url: zip_bytes}))


def test_happy_path_liefert_gueltige_messwerte_ohne_hinweise() -> None:
    importer = _importer_mit_fixture()
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    ergebnis = importer.importiere(_STATION_ID, zeitraum)

    assert len(ergebnis.messwerte) == 5
    assert ergebnis.verwendeter_zeitraum == zeitraum
    assert ergebnis.hinweise == []


def test_zeitraum_teilweise_ausserhalb_wird_gekuerzt_und_hinweis_gesetzt() -> None:
    importer = _importer_mit_fixture()
    zeitraum = Zeitraum(start=date(2014, 6, 1), ende=date(2020, 1, 1))

    ergebnis = importer.importiere(_STATION_ID, zeitraum)

    assert ergebnis.verwendeter_zeitraum == Zeitraum(start=date(2015, 1, 1), ende=date(2020, 1, 1))
    assert len(ergebnis.messwerte) == 5
    assert any("gekürzt" in hinweis for hinweis in ergebnis.hinweise)


def test_fehlerhafte_datensaetze_werden_verworfen_gueltige_bleiben() -> None:
    importer = _importer_mit_fixture()
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    ergebnis = importer.importiere(_STATION_ID, zeitraum)

    werte = [messwert.wert for messwert in ergebnis.messwerte]
    assert -999.0 not in werte
    assert len(werte) == 5


def test_datenluecke_liefert_leeres_ergebnis_mit_hinweis() -> None:
    importer = _importer_mit_fixture()
    zeitraum = Zeitraum(start=date(2021, 6, 1), ende=date(2021, 6, 2))

    ergebnis = importer.importiere(_STATION_ID, zeitraum)

    assert ergebnis.messwerte == []
    assert any(
        "Datenlücke" in hinweis or "keine Messwerte" in hinweis for hinweis in ergebnis.hinweise
    )


# --- Destructive QA: DQA-1 (FR-006, Zeitraum vollständig außerhalb des unterstützten Bereichs) ---


def test_zeitraum_vollstaendig_vor_unterstuetztem_bereich_stuerzt_nicht_ab() -> None:
    """FR-006: Ein Zeitraum vollständig VOR 01.01.2015 darf den Import nicht zum Absturz bringen."""
    importer = _importer_mit_fixture()
    zeitraum = Zeitraum(start=date(2010, 1, 1), ende=date(2010, 12, 31))

    ergebnis = importer.importiere(_STATION_ID, zeitraum)

    assert ergebnis.messwerte == []


def test_zeitraum_vollstaendig_nach_unterstuetztem_bereich_stuerzt_nicht_ab() -> None:
    """FR-006: Ein Zeitraum vollständig NACH 31.12.2025 darf den Import nicht abstürzen lassen."""
    importer = _importer_mit_fixture()
    zeitraum = Zeitraum(start=date(2026, 1, 1), ende=date(2026, 12, 31))

    ergebnis = importer.importiere(_STATION_ID, zeitraum)

    assert ergebnis.messwerte == []


# --- Destructive QA: DQA-2 (FR-007, ungültiges MESS_DATUM darf nicht zum Absturz führen) ---

_FIXTURE_DEFEKTES_MESS_DATUM = (
    Path(__file__).resolve().parents[1]
    / "fixtures"
    / "dwd"
    / "10minutenwerte_TU_00099_defekt_mess_datum_hist.zip"
)


def test_datensatz_mit_defektem_mess_datum_wird_uebersprungen_statt_absturz() -> None:
    """FR-007: Formatfehler in MESS_DATUM muss den Datensatz überspringen, nicht abstürzen."""
    zip_bytes = _FIXTURE_DEFEKTES_MESS_DATUM.read_bytes()
    url = ZIP_URL_TEMPLATE.format(station_id="00099")
    importer = LufttemperaturImporter(FakeHttpClient({url: zip_bytes}))
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    ergebnis = importer.importiere("00099", zeitraum)

    assert len(ergebnis.messwerte) == 2
