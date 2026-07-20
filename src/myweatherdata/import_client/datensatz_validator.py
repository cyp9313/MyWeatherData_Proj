"""Validierung roher DWD-Datensätze für den Lufttemperatur-Import (FR-007)."""

from __future__ import annotations

from datetime import datetime

_PFLICHTFELDER = ("STATIONS_ID", "MESS_DATUM", "TT_10")
_FEHLWERT = -999.0
_ZEITSTEMPEL_FORMAT = "%Y%m%d%H%M"


class DatensatzValidator:
    """Erkennt fehlerhafte/unvollständige rohe DWD-Datensätze (FR-007)."""

    def validiere(self, rohdatensatz: dict[str, str]) -> bool:
        """Prüft, ob der rohe Datensatz vollständig, formatgültig und kein Fehlwert ist."""
        if any(feld not in rohdatensatz for feld in _PFLICHTFELDER):
            return False

        try:
            datetime.strptime(rohdatensatz["MESS_DATUM"], _ZEITSTEMPEL_FORMAT)
        except ValueError:
            return False

        try:
            temperatur = float(rohdatensatz["TT_10"])
        except ValueError:
            return False

        return temperatur != _FEHLWERT
