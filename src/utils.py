"""
Утилиты для работы с JSON-файлами.
"""

import json
import os
from typing import Any, Dict, List


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с транзакциями.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список словарей. При ошибке, пустом файле или не-списке — пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        return []
    except (json.JSONDecodeError, IOError):
        return []
    