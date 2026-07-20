"""Gemeinsame Pytest-Fixtures und Test-Doubles für die Import-Client-Testsuite."""

from __future__ import annotations


class FakeHttpClient:
    """Test-Double für den Port `HttpClient` (url -> bytes | Exception).

    Greift NIE auf das echte Netzwerk zu; die Antworten je URL werden beim
    Erzeugen fest hinterlegt.
    """

    def __init__(self, antworten: dict[str, bytes | Exception]) -> None:
        self._antworten = antworten

    def get_bytes(self, url: str) -> bytes:
        antwort = self._antworten[url]
        if isinstance(antwort, Exception):
            raise antwort
        return antwort
