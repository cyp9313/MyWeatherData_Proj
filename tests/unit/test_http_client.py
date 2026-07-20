"""Tests für `RequestsHttpClient` (HTTP-Adapter, Port-Grenze zu `HttpClientError`)."""

from __future__ import annotations

from unittest.mock import Mock, patch

import pytest
import requests

from myweatherdata.import_client.http_client import RequestsHttpClient
from myweatherdata.ports.http_client_port import HttpClientError


def test_get_bytes_liefert_response_inhalt_bei_erfolg() -> None:
    fake_response = Mock()
    fake_response.content = b"raw-bytes"
    fake_response.raise_for_status = Mock()

    with patch(
        "myweatherdata.import_client.http_client.requests.get",
        return_value=fake_response,
    ):
        ergebnis = RequestsHttpClient().get_bytes("https://example.invalid/datei")

    assert ergebnis == b"raw-bytes"


def test_get_bytes_wandelt_request_exception_in_http_client_error_um() -> None:
    with patch(
        "myweatherdata.import_client.http_client.requests.get",
        side_effect=requests.RequestException("Netzwerkfehler"),
    ):
        with pytest.raises(HttpClientError):
            RequestsHttpClient().get_bytes("https://example.invalid/datei")
