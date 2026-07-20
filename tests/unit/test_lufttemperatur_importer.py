"""Tests für `LufttemperaturImporter` (FR-005, FR-006, FR-007, FR-008)."""

from __future__ import annotations

import io
import zipfile
from datetime import date
from pathlib import Path

from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.lufttemperatur_importer import (
    HISTORICAL_VERZEICHNIS_URL,
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


def _dateiname(station_id: str) -> str:
    """Synthetischer, aber real-konformer Dateiname (Muster: Design-Entscheidung Phase 7R)."""
    return f"10minutenwerte_TU_{station_id}_20150101_20251231_hist.zip"


def _listing_html(station_id: str) -> bytes:
    return f'<a href="{_dateiname(station_id)}">...</a>'.encode("latin-1")


def _http_client_mit_zip(station_id: str, zip_bytes: bytes) -> FakeHttpClient:
    return FakeHttpClient(
        {
            HISTORICAL_VERZEICHNIS_URL: _listing_html(station_id),
            HISTORICAL_VERZEICHNIS_URL + _dateiname(station_id): zip_bytes,
        }
    )


def _importer_mit_fixture() -> LufttemperaturImporter:
    zip_bytes = _FIXTURE_PFAD.read_bytes()
    return LufttemperaturImporter(_http_client_mit_zip(_STATION_ID, zip_bytes))


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
    importer = LufttemperaturImporter(_http_client_mit_zip("00099", zip_bytes))
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    ergebnis = importer.importiere("00099", zeitraum)

    assert len(ergebnis.messwerte) == 2


# --- Destructive QA (Phase 10R): DQA-5 (Messwert.station_id inkonsistent) ---


def _real_formatiertes_zip(stations_id_feld: str) -> bytes:
    """Baut ein ZIP mit real-konform rechtsbündiger STATIONS_ID-Spalte (siehe
    `doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 2, und die real-basierte
    Fixture `10minutenwerte_TU_00003_real_auszug_hist.zip`)."""
    header = "STATIONS_ID;MESS_DATUM;  QN;PP_10;TT_10;TM5_10;RF_10;TD_10;eor"
    zeile = f"{stations_id_feld};202001010000;    3;  970.2;   5.4;   5.0;  80.0;   3.1;eor"
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w") as zf:
        inhalt = header + "\r\n" + zeile + "\r\n"
        zf.writestr("produkt_zehn_min_tu_20150101_20251231_00003.txt", inhalt)
    return puffer.getvalue()


def test_messwert_station_id_entspricht_angefragter_stations_id_trotz_realer_formatierung() -> None:
    """Die reale STATIONS_ID-Spalte ist rechtsbündig ohne führende Nullen (Contract Baseline
    Abschnitt 2, bereits als Kontraktbefund in `test_dwd_zip_reader.py` dokumentiert). Trotzdem
    muss `Messwert.station_id` der angefragten, führende-Nullen-erhaltenden Stations-ID
    entsprechen, damit sie zu `ImportErgebnis.station.station_id` (vom
    `LufttemperaturImportKoordinator` gesetzt, siehe `import_koordinator.py`) passt."""
    zip_bytes = _real_formatiertes_zip("          3")
    importer = LufttemperaturImporter(_http_client_mit_zip("00003", zip_bytes))
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    ergebnis = importer.importiere("00003", zeitraum)

    assert len(ergebnis.messwerte) == 1
    assert ergebnis.messwerte[0].station_id == "00003"
