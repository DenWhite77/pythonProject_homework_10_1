"""Тесты для модуля generators."""

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            "id": 939719570,
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2


def test_filter_by_currency_rub(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "RUB"))
    assert len(result) == 1


def test_filter_by_currency_not_found(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(result) == 0


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]
    assert descriptions == expected


def test_transaction_descriptions_empty():
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_single():
    result = list(card_number_generator(42, 42))
    assert result == ["0000 0000 0000 0042"]
