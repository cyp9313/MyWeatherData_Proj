"""Tests für `dwd_zip_reader` (FR-005)."""

from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pytest

from myweatherdata.import_client.dwd_zip_reader import DwdZipFormatError, lese_rohdatensaetze

_FIXTURE_PFAD = (
    Path(__file__).resolve().parents[1]
    / "fixtures"
    / "dwd"
    / "10minutenwerte_TU_00003_beispiel_hist.zip"
)


def test_gueltiges_zip_fixture_wird_korrekt_eingelesen() -> None:
    zip_bytes = _FIXTURE_PFAD.read_bytes()

    rohdatensaetze = lese_rohdatensaetze(zip_bytes)

    assert len(rohdatensaetze) == 7
    assert rohdatensaetze[0]["STATIONS_ID"] == "00003"
    assert rohdatensaetze[0]["MESS_DATUM"] == "202001010000"
    assert rohdatensaetze[0]["TT_10"] == "5.4"


def test_zip_ohne_produkt_datei_wirft_dwd_zip_format_error() -> None:
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w") as zf:
        zf.writestr("Metadaten_Geographie_00003.txt", "irrelevanter Inhalt")

    with pytest.raises(DwdZipFormatError):
        lese_rohdatensaetze(puffer.getvalue())


# --- Destructive QA: DQA-4 (ZIP mit mehreren Produktdateien ist mehrdeutig) ---


def test_zip_mit_mehreren_produkt_dateien_wirft_dwd_zip_format_error() -> None:
    """DQA-4: Mehrere `produkt_*`-Dateien widersprechen der dokumentierten
    Annahme ("genau eine Datei") und müssen als Formatfehler erkannt werden,
    statt eine der beiden Dateien willkürlich zu verwenden."""
    header = "STATIONS_ID;MESS_DATUM;QN;PP_10;TT_10;TM5_10;RF_10;TD_10;eor"
    puffer = io.BytesIO()
    with zipfile.ZipFile(puffer, "w") as zf:
        zf.writestr(
            "produkt_zehn_min_tu_20200101_20200101_00003.txt",
            header + "\r\n00003;202001010000;3;1013.1;5.4;5.0;80;3.1;eor\r\n",
        )
        zf.writestr(
            "produkt_zehn_min_tu_19500101_20211231_00003.txt",
            header + "\r\n00003;195001010000;3;1013.1;9.9;5.0;80;3.1;eor\r\n",
        )

    with pytest.raises(DwdZipFormatError):
        lese_rohdatensaetze(puffer.getvalue())
