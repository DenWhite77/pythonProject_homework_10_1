"""
Утилиты для работы с JSON-файлами.
"""

import json
import logging
import os
from typing import Any, Dict, List

# Создаём папку для логов, если её нет
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(os.path.join(LOG_DIR, 'utils.log'), mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger_utils.addHandler(file_handler)


def read_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с транзакциями.

    Args:
        file_path: Путь к JSON-файлу

    Returns:
        Список словарей. При ошибке, пустом файле или не-списке — пустой список.
    """
    logger_utils.debug(f"Попытка чтения файла: {file_path}")

    if not os.path.exists(file_path):
        logger_utils.error(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if isinstance(data, list):
            logger_utils.info(f"Файл {file_path} успешно прочитан, количество записей: {len(data)}")
            return data
        else:
            logger_utils.error(f"Файл {file_path} не содержит список. Тип данных: {type(data).__name__}")
            return []
    except json.JSONDecodeError as e:
        logger_utils.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []
    except IOError as e:
        logger_utils.error(f"Ошибка ввода-вывода при чтении файла {file_path}: {e}")
        return []
