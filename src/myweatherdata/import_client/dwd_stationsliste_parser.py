"""Parser für die fixed-width DWD-Stationsliste (`help`-Verzeichnis, FR-001).

Format-Verifikation (Real-DWD Contract Spike, Phase 5.5, siehe
`doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 1): Kopfzeile mit
Spaltennamen, gefolgt von einer Trennzeile aus Bindestrichen (deren Länge NICHT
die tatsächlichen Spaltenbreiten der Datenzeilen wiedergibt - sie stimmt nur
zufällig für `Stationsname` überein), gefolgt von fixed-width Datenzeilen mit
festen Byte-Offsets: `Stations_id` [0,5), `von_datum` [6,14), `bis_datum`
[15,23), `Stationshoehe` (rechtsbündig, Ende immer bei Spalte 38), `geoBreite`
(rechtsbündig, Ende immer bei Spalte 50), `geoLaenge` (rechtsbündig, Ende immer
bei Spalte 60), `Stationsname` (fester 41-Zeichen-Slot [61,102)), `Bundesland`
(fester 41-Zeichen-Slot [102,143)). Diese Offsets sind gegen eine live
heruntergeladene DWD-Datei verifiziert (siehe reale Fixture
`tests/fixtures/dwd/stationsliste_real_auszug.txt`).
"""

from __future__ import annotations

from dataclasses import dataclass

from myweatherdata.domain.koordinate import Koordinate

_STATION_ID_ENDE = 5
_VON_DATUM_START = 6
_VON_DATUM_ENDE = 14
_BIS_DATUM_START = 15
_BIS_DATUM_ENDE = 23
_STATIONSHOEHE_ENDE = 38
_GEOBREITE_ENDE = 50
_GEOLAENGE_ENDE = 60
_NAME_START = 61
_NAME_ENDE = 102
_BUNDESLAND_START = 102
_BUNDESLAND_ENDE = 143


@dataclass(frozen=True)
class StationsListenEintrag:
    """Ein Eintrag der geparsten DWD-Stationsliste."""

    station_id: str
    name: str
    koordinate: Koordinate


def parse_stationsliste(inhalt: str) -> list[StationsListenEintrag]:
    """Parst den Rohtext der DWD-Stationsliste in eine Liste von Einträgen."""
    zeilen = inhalt.splitlines()
    if len(zeilen) < 2:
        return []

    eintraege: list[StationsListenEintrag] = []
    for zeile in zeilen[2:]:
        if not zeile.strip():
            continue
        eintrag = _zeile_zu_eintrag(zeile)
        if eintrag is not None:
            eintraege.append(eintrag)
    return eintraege


def _zeile_zu_eintrag(zeile: str) -> StationsListenEintrag | None:
    if len(zeile) < _BUNDESLAND_ENDE:
        return None

    station_id = zeile[:_STATION_ID_ENDE].strip()
    stationshoehe_feld = zeile[_BIS_DATUM_ENDE:_STATIONSHOEHE_ENDE].strip()
    geobreite_feld = zeile[_STATIONSHOEHE_ENDE:_GEOBREITE_ENDE].strip()
    geolaenge_feld = zeile[_GEOBREITE_ENDE:_GEOLAENGE_ENDE].strip()
    name = zeile[_NAME_START:_NAME_ENDE].strip()

    if not station_id or not stationshoehe_feld:
        return None

    try:
        koordinate = Koordinate(
            breitengrad=float(geobreite_feld),
            laengengrad=float(geolaenge_feld),
        )
    except ValueError:
        return None

    return StationsListenEintrag(station_id=station_id, name=name, koordinate=koordinate)
