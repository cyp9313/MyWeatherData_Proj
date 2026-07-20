"""Tests für die ZIP-Ermittlung über das reale DWD-Verzeichnis-Listing (Phase 7R).

Siehe Design-Entscheidung in `pjm/import-client-implementation-plan.md`,
Abschnitt "Design-Entscheidung Phase 7R".
"""

from __future__ import annotations

from datetime import date

from myweatherdata.domain.zeitraum import Zeitraum
from myweatherdata.import_client.dwd_archiv_verzeichnis import (
    passende_zip_dateinamen,
    zip_dateinamen_aus_listing,
)

_LISTING_AUSZUG = """
<html><body>
<a href="10minutenwerte_TU_00003_19930428_19991231_hist.zip">...</a>
<a href="10minutenwerte_TU_00003_20000101_20091231_hist.zip">...</a>
<a href="10minutenwerte_TU_00003_20100101_20110331_hist.zip">...</a>
<a href="10minutenwerte_TU_00044_20070208_20260720_hist.zip">...</a>
</body></html>
"""


def test_zip_dateinamen_aus_listing_liefert_nur_dateien_der_gesuchten_station() -> None:
    dateinamen = zip_dateinamen_aus_listing(_LISTING_AUSZUG, station_id="00003")

    assert dateinamen == [
        "10minutenwerte_TU_00003_19930428_19991231_hist.zip",
        "10minutenwerte_TU_00003_20000101_20091231_hist.zip",
        "10minutenwerte_TU_00003_20100101_20110331_hist.zip",
    ]


def test_zip_dateinamen_aus_listing_liefert_leere_liste_ohne_treffer() -> None:
    dateinamen = zip_dateinamen_aus_listing(_LISTING_AUSZUG, station_id="99999")

    assert dateinamen == []


def test_passende_zip_dateinamen_waehlt_ueberschneidenden_zeitraum() -> None:
    dateinamen = [
        "10minutenwerte_TU_00003_19930428_19991231_hist.zip",
        "10minutenwerte_TU_00003_20000101_20091231_hist.zip",
        "10minutenwerte_TU_00003_20100101_20110331_hist.zip",
    ]
    zeitraum = Zeitraum(start=date(2010, 6, 1), ende=date(2010, 6, 1))

    passende = passende_zip_dateinamen(dateinamen, zeitraum)

    assert passende == ["10minutenwerte_TU_00003_20100101_20110331_hist.zip"]


def test_passende_zip_dateinamen_liefert_mehrere_bei_ueberlappung_ueber_dateigrenze() -> None:
    dateinamen = [
        "10minutenwerte_TU_00003_20000101_20091231_hist.zip",
        "10minutenwerte_TU_00003_20100101_20110331_hist.zip",
    ]
    zeitraum = Zeitraum(start=date(2009, 12, 1), ende=date(2010, 1, 15))

    passende = passende_zip_dateinamen(dateinamen, zeitraum)

    assert passende == [
        "10minutenwerte_TU_00003_20000101_20091231_hist.zip",
        "10minutenwerte_TU_00003_20100101_20110331_hist.zip",
    ]


def test_passende_zip_dateinamen_liefert_leere_liste_ohne_ueberschneidung() -> None:
    dateinamen = ["10minutenwerte_TU_00003_20100101_20110331_hist.zip"]
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 1, 1))

    passende = passende_zip_dateinamen(dateinamen, zeitraum)

    assert passende == []
