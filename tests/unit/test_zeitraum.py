"""Tests für das Wertobjekt `Zeitraum` (FR-005, FR-006)."""

from __future__ import annotations

from datetime import date

import pytest

from myweatherdata.domain.zeitraum import Zeitraum


def test_zeitraum_vollstaendig_im_unterstuetzten_bereich_liefert_true() -> None:
    zeitraum = Zeitraum(start=date(2020, 1, 1), ende=date(2020, 12, 31))

    assert zeitraum.liegt_vollstaendig_im_unterstuetzten_bereich() is True


def test_zeitraum_teilweise_ausserhalb_liefert_false() -> None:
    zeitraum = Zeitraum(start=date(2014, 6, 1), ende=date(2015, 6, 1))

    assert zeitraum.liegt_vollstaendig_im_unterstuetzten_bereich() is False


def test_zeitraum_teilweise_ausserhalb_wird_auf_unterstuetzten_bereich_gekuerzt() -> None:
    zeitraum = Zeitraum(start=date(2014, 6, 1), ende=date(2015, 6, 1))

    gekuerzt = zeitraum.gekuerzt_auf_unterstuetzten_bereich()

    assert gekuerzt == Zeitraum(start=date(2015, 1, 1), ende=date(2015, 6, 1))


def test_zeitraum_start_nach_ende_wirft_value_error() -> None:
    with pytest.raises(ValueError):
        Zeitraum(start=date(2020, 1, 2), ende=date(2020, 1, 1))
