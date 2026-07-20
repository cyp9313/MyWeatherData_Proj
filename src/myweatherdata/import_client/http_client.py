"""HTTP-Adapter (`RequestsHttpClient`) für den Import-Client.

Fängt gezielt `requests.RequestException` und wandelt sie in die
technologieneutrale `HttpClientError` (Port-Ebene) um. `requests`-spezifische
Exceptions verlassen den Adapter nie als Cross-Layer-Kontrakt (kein
`except Exception`).
"""

from __future__ import annotations

import requests

from myweatherdata.ports.http_client_port import HttpClientError

_TIMEOUT_SEKUNDEN = 30


class RequestsHttpClient:
    """Realisiert den Port `HttpClient` mittels der Bibliothek `requests`."""

    def get_bytes(self, url: str) -> bytes:
        """Lädt den Inhalt der übergebenen URL als Rohbytes."""
        try:
            response = requests.get(url, timeout=_TIMEOUT_SEKUNDEN)
            response.raise_for_status()
        except requests.RequestException as fehler:
            raise HttpClientError(f"HTTP-Zugriff auf {url} fehlgeschlagen: {fehler}") from fehler
        return response.content
