"""Liest die Rohdatensätze aus einer DWD-Messdaten-ZIP-Datei (FR-005).

Format gegen einen echten Live-Abruf verifiziert (Real-DWD Contract Spike,
Phase 5.5, siehe `doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 2): Die
ZIP-Datei enthält genau eine Datei mit Präfix `produkt_`, deren Inhalt eine
`;`-getrennte, `latin-1`-kodierte CSV-Datei mit Kopfzeile ist.
"""

from __future__ import annotations

import csv
import io
import zipfile

_PRODUKT_DATEI_PRAEFIX = "produkt_"


class DwdZipFormatError(Exception):
    """Technischer Fehler beim Lesen einer DWD-ZIP-Datei (unerwarteter Inhalt)."""


def lese_rohdatensaetze(zip_bytes: bytes) -> list[dict[str, str]]:
    """Liest die Produktdatei aus der ZIP und liefert deren Zeilen als Rohdatensätze."""
    try:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archiv:
            produkt_dateiname = _finde_produkt_datei(archiv)
            inhalt = archiv.read(produkt_dateiname).decode("latin-1")
    except zipfile.BadZipFile as fehler:
        raise DwdZipFormatError(f"Ungültige ZIP-Datei: {fehler}") from fehler

    reader = csv.DictReader(io.StringIO(inhalt), delimiter=";")
    # `csv.DictReader` befüllt bei einer Zeile mit weniger Feldern als die Kopfzeile
    # fehlende Werte mit `None` (restval) und sammelt bei mehr Feldern als die Kopfzeile
    # die überzähligen Werte unter dem Schlüssel `None` (restkey). Beides sind reguläre,
    # nicht crashende Fälle unvollständiger/zusätzlicher Spalten (FR-007): fehlende Werte
    # werden als leerer String abgebildet (von `DatensatzValidator` als ungültig erkannt),
    # der `restkey`-Eintrag mit unbekannten Spalten wird ignoriert.
    return [
        {
            schluessel.strip(): wert.strip() if wert is not None else ""
            for schluessel, wert in zeile.items()
            if schluessel is not None
        }
        for zeile in reader
    ]


def _finde_produkt_datei(archiv: zipfile.ZipFile) -> str:
    kandidaten = [name for name in archiv.namelist() if name.startswith(_PRODUKT_DATEI_PRAEFIX)]
    if not kandidaten:
        raise DwdZipFormatError(
            f"Keine Datei mit Präfix '{_PRODUKT_DATEI_PRAEFIX}' im ZIP-Archiv gefunden."
        )
    if len(kandidaten) > 1:
        raise DwdZipFormatError(
            f"Mehrdeutiger Inhalt: mehrere Dateien mit Präfix '{_PRODUKT_DATEI_PRAEFIX}' "
            f"im ZIP-Archiv gefunden: {kandidaten}."
        )
    return kandidaten[0]
