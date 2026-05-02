"""Модуль с генераторами для работы с транзакциями."""

from typing import Dict, Generator, List, Any


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """
    Фильтрует транзакции по заданной валюте.

    Args:
        transactions: Список словарей с транзакциями
        currency: Код валюты для фильтрации (например, 'USD', 'RUB')

    Yields:
        Транзакции, где валюта соответствует заданной
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Генератор описаний транзакций.

    Args:
        transactions: Список словарей с транзакциями

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальное значение диапазона
        stop: Конечное значение диапазона (включительно)

    Yields:
        Отформатированный номер карты
    """
    for number in range(start, stop + 1):
        formatted = f"{number:016d}"
        groups = [formatted[i:i+4] for i in range(0, 16, 4)]
        yield " ".join(groups)
