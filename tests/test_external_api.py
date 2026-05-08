"""
Тесты для модуля external_api.
"""

import os
from unittest.mock import patch

import pytest

from src.external_api import convert_currency

from requests.exceptions import RequestException


@pytest.fixture
def usd_transaction():
    """Фикстура: транзакция в USD."""
    return {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}


@pytest.fixture
def eur_transaction():
    """Фикстура: транзакция в EUR."""
    return {"operationAmount": {"amount": "50.00", "currency": {"code": "EUR"}}}


@pytest.fixture
def rub_transaction():
    """Фикстура: транзакция в RUB."""
    return {"operationAmount": {"amount": "5000.00", "currency": {"code": "RUB"}}}


@patch("src.external_api.requests.get")
def test_convert_usd_to_rub(mock_get, usd_transaction):
    """Тест конвертации USD → RUB."""
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"rates": {"RUB": 90.5}}
    mock_response.raise_for_status.return_value = None

    with patch.dict(os.environ, {"EXCHANGE_API_KEY": "fake_key"}):
        result = convert_currency(usd_transaction)

    expected = 100.00 * 90.5
    assert result == expected


@patch("src.external_api.requests.get")
def test_convert_eur_to_rub(mock_get, eur_transaction):
    """Тест конвертации EUR → RUB."""
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"rates": {"RUB": 98.3}}
    mock_response.raise_for_status.return_value = None

    with patch.dict(os.environ, {"EXCHANGE_API_KEY": "fake_key"}):
        result = convert_currency(eur_transaction)

    expected = 50.00 * 98.3
    assert result == expected


def test_convert_rub_no_api(rub_transaction):
    """Тест: рублёвая транзакция — без вызова API."""
    result = convert_currency(rub_transaction)
    assert result == 5000.00


@patch("src.external_api.requests.get")
def test_convert_api_failure(mock_get, usd_transaction):
    """Тест: при ошибке API возвращается исходная сумма."""
    mock_get.side_effect = RequestException("API error")

    with patch.dict(os.environ, {"EXCHANGE_API_KEY": "fake_key"}):
        result = convert_currency(usd_transaction)

    assert result == 100.00


def test_convert_no_api_key(usd_transaction):
    """Тест: если нет API-ключа, возвращается исходная сумма."""
    with patch.dict(os.environ, {}, clear=True):
        result = convert_currency(usd_transaction)

    assert result == 100.00


@patch("src.external_api.requests.get")
def test_convert_unsupported_currency(mock_get):
    """Тест: неподдерживаемая валюта — без вызова API."""
    transaction = {"operationAmount": {"amount": "200", "currency": {"code": "GBP"}}}

    result = convert_currency(transaction)

    assert result == 200.00
    mock_get.assert_not_called()
