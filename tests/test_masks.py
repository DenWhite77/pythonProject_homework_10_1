import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "1234 56** **** 3456"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("12345678901234567890", "1234 56** **** 7890"),
])
def test_get_mask_card_number(card_number, expected):
    """Тест маскирования номера карты"""
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_empty():
    """Тест с пустой строкой"""
    assert get_mask_card_number("") == " ** **** "


@pytest.mark.parametrize("account_number, expected", [
    ("12345678901234567890", "**7890"),
    ("12345", "**2345"),  # Исправлено: последние 4 цифры "2345"
    ("", "**"),
])
def test_get_mask_account(account_number, expected):
    """Тест маскирования номера счета"""
    assert get_mask_account(account_number) == expected
