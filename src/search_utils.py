"""
Модуль для поиска транзакций по описанию с использованием регулярных выражений.
"""

import re
from typing import List, Dict, Any


def search_transactions(transactions: List[Dict[str, Any]], search_query: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции, в описании которых содержится искомая строка (регистронезависимо).

    Args:
        transactions: Список словарей с транзакциями.
        search_query: Строка для поиска.

    Returns:
        Список транзакций, удовлетворяющих условию поиска.
    """
    if not transactions or not search_query:
        return []

    pattern = re.compile(re.escape(search_query), re.IGNORECASE)
    result = []

    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)

    return result
