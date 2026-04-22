import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("Maestro 1111222233334444", "Maestro 1111 22** **** 4444"),
])
def test_mask_account_card(input_str, expected):
    """Тест маскирования карт и счетов"""
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-11T12:30:45", "11.03.2024"),
    ("2023-12-25T08:15:00", "25.12.2023"),
])
def test_get_date(date_str, expected):
    """Тест преобразования даты"""
    assert get_date(date_str) == expected


def test_get_date_invalid():
    """Тест с некорректной датой"""
    assert get_date("invalid") == "Неверный формат"
