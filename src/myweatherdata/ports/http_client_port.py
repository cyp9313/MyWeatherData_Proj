"""Technologieneutraler Port für HTTP-Zugriffe des Import-Client-Adapters."""

from __future__ import annotations

from typing import Protocol


class HttpClientError(Exception):
    """Technologieneutraler Fehler bei einem HTTP-Zugriff (Port-Grenze).

    Wird von Adaptern (z. B. `RequestsHttpClient`) aus technologiespezifischen
    Exceptions (z. B. `requests.RequestException`) erzeugt. Kein
    technologiespezifischer Exception-Typ darf diese Port-Grenze überqueren.
    """


class HttpClient(Protocol):
    """Port für einen HTTP-Client, der Rohbytes von einer URL lädt."""

    def get_bytes(self, url: str) -> bytes:
        """Lädt den Inhalt der übergebenen URL als Rohbytes."""
        ...
