"""
Модуль для подсчёта количества транзакций по категориям.
"""

from collections import Counter
from typing import List, Dict, Any


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество транзакций в каждой категории на основе поля description.

    Args:
        transactions: Список словарей с транзакциями.
        categories: Список категорий для подсчёта.

    Returns:
        Словарь: {категория: количество транзакций}
    """
    if not transactions or not categories:
        return {category: 0 for category in categories}

    categories_lower = [cat.lower() for cat in categories]
    filtered = []

    for transaction in transactions:
        description = transaction.get("description", "").lower()
        if description in categories_lower:
            filtered.append(description)

    counter = Counter(filtered)

    result = {}
    for i, category in enumerate(categories):
        result[category] = counter.get(categories_lower[i], 0)

    return result
