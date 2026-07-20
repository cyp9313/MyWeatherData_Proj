"""Parser für die fixed-width DWD-Stationsliste (`help`-Verzeichnis, FR-001).

Format-Annahme (technischer Spike, siehe arc/statische_sichten/klassensicht.md,
Abschnitt "Weitere Confirmation-Punkte", Nr. 4): Kopfzeile mit Spaltennamen,
gefolgt von einer Trennzeile aus Bindestrichen je Spalte (deren Länge die
Spaltenbreite vorgibt), gefolgt von fixed-width Datenzeilen mit den Spalten
`Stations_id`, `von_datum`, `bis_datum`, `Stationshoehe`, `geoBreite`,
`geoLaenge`, `Stationsname`, `Bundesland`. Diese Annahme ist noch nicht gegen
eine live heruntergeladene DWD-Datei verifiziert (offener Punkt).
"""

from __future__ import annotations

from dataclasses import dataclass

from myweatherdata.domain.koordinate import Koordinate

_SPALTEN_REIHENFOLGE = (
    "station_id",
    "von_datum",
    "bis_datum",
    "stationshoehe",
    "geobreite",
    "geolaenge",
    "name",
    "bundesland",
)


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

    spaltenbreiten = [len(gruppe) for gruppe in zeilen[1].split(" ")]

    eintraege: list[StationsListenEintrag] = []
    for zeile in zeilen[2:]:
        if not zeile.strip():
            continue
        werte = _zeile_in_spalten_zerlegen(zeile, spaltenbreiten)
        felder = dict(zip(_SPALTEN_REIHENFOLGE, werte, strict=False))
        try:
            koordinate = Koordinate(
                breitengrad=float(felder["geobreite"].strip()),
                laengengrad=float(felder["geolaenge"].strip()),
            )
        except ValueError:
            continue
        eintraege.append(
            StationsListenEintrag(
                station_id=felder["station_id"].strip(),
                name=felder["name"].strip(),
                koordinate=koordinate,
            )
        )
    return eintraege


def _zeile_in_spalten_zerlegen(zeile: str, spaltenbreiten: list[int]) -> list[str]:
    werte: list[str] = []
    position = 0
    for breite in spaltenbreiten:
        werte.append(zeile[position : position + breite])
        position += breite + 1
    return werte
