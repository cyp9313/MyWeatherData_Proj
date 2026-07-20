"""Tests für den `DatensatzValidator` (FR-007)."""

from __future__ import annotations

from myweatherdata.import_client.datensatz_validator import DatensatzValidator


def test_gueltiger_rohdatensatz_besteht_validierung() -> None:
    rohdatensatz = {
        "STATIONS_ID": "00003",
        "MESS_DATUM": "201501010000",
        "QN": "3",
        "PP_10": "1013.2",
        "TT_10": "5.4",
        "TM5_10": "5.0",
        "RF_10": "80.0",
        "TD_10": "2.1",
        "eor": "eor",
    }

    assert DatensatzValidator().validiere(rohdatensatz) is True


def test_rohdatensatz_mit_fehlwert_besteht_validierung_nicht() -> None:
    rohdatensatz = {
        "STATIONS_ID": "00003",
        "MESS_DATUM": "201501010000",
        "QN": "3",
        "PP_10": "1013.2",
        "TT_10": "-999",
        "TM5_10": "5.0",
        "RF_10": "80.0",
        "TD_10": "2.1",
        "eor": "eor",
    }

    assert DatensatzValidator().validiere(rohdatensatz) is False


def test_unvollstaendiger_rohdatensatz_besteht_validierung_nicht() -> None:
    rohdatensatz = {
        "STATIONS_ID": "00003",
        "MESS_DATUM": "201501010000",
        "QN": "3",
        "PP_10": "1013.2",
        # TT_10 fehlt
        "TM5_10": "5.0",
        "RF_10": "80.0",
        "TD_10": "2.1",
        "eor": "eor",
    }

    assert DatensatzValidator().validiere(rohdatensatz) is False


def test_rohdatensatz_mit_defektem_mess_datum_besteht_validierung_nicht() -> None:
    """DQA-2 (FR-007): Formatfehler in MESS_DATUM muss als fehlerhaft erkannt werden."""
    rohdatensatz = {
        "STATIONS_ID": "00003",
        "MESS_DATUM": "ABCDEFGHIJKL",
        "QN": "3",
        "PP_10": "1013.2",
        "TT_10": "5.4",
        "TM5_10": "5.0",
        "RF_10": "80.0",
        "TD_10": "2.1",
        "eor": "eor",
    }

    assert DatensatzValidator().validiere(rohdatensatz) is False
