"""Liest die Rohdatensätze aus einer DWD-Messdaten-ZIP-Datei (FR-005).

Format-Annahme (technischer Spike, siehe arc/statische_sichten/klassensicht.md,
Abschnitt "Weitere Confirmation-Punkte", Nr. 4): Die ZIP-Datei enthält neben
Metadaten-Dateien genau eine Datei mit Präfix `produkt_`, deren Inhalt eine
`;`-getrennte CSV-Datei mit Kopfzeile ist (siehe
doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md).
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
    return [
        {schluessel.strip(): wert.strip() for schluessel, wert in zeile.items()} for zeile in reader
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
