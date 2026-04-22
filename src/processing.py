from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Args:
        data: Исходный список словарей.
        state: Значение state для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Новый список словарей, содержащий только элементы с указанным state.
    """
    return [item for item in data if item.get('state') == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.

    Args:
        data: Исходный список словарей.
        descending: Порядок сортировки. True — по убыванию (сначала новые), False — по возрастанию.

    Returns:
        Новый отсортированный список словарей.
    """
    return sorted(data, key=lambda item: item['date'], reverse=descending)
