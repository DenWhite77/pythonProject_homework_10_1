"""Тесты для модуля external_api."""

import os
from unittest.mock import patch

import pytest
from requests.exceptions import RequestException

from src.external_api import convert_currency


@pytest.fixture
def usd_transaction():
    return {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get, usd_transaction):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.5}}
    mock_get.return_value.raise_for_status.return_value = None

    with patch.dict(os.environ, {"EXCHANGE_API_KEY": "fake"}):
        result = convert_currency(usd_transaction)

    assert result == 9050.0


@patch("src.external_api.requests.get")
def test_convert_api_failure(mock_get, usd_transaction):
    mock_get.side_effect = RequestException("API error")

    with patch.dict(os.environ, {"EXCHANGE_API_KEY": "fake"}):
        result = convert_currency(usd_transaction)

    assert result == 100.0
