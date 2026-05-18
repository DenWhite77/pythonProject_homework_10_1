"""
Модуль для чтения финансовых транзакций из CSV и Excel файлов.
"""

from typing import Any, Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из CSV-файла и возвращает список словарей.

    Args:
        file_path: Путь к CSV-файлу.

    Returns:
        Список словарей с данными транзакций. При ошибке возвращает пустой список.
    """
    try:
        df = pd.read_csv(file_path, sep=';')
        print(f"CSV загружен, строк: {len(df)}")
        print(f"Колонки: {list(df.columns)}")
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает транзакции из Excel-файла (xlsx) и возвращает список словарей.

    Args:
        file_path: Путь к Excel-файлу.

    Returns:
        Список словарей с данными транзакций. При ошибке возвращает пустой список.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df.to_dict(orient='records')  # type: ignore[return-value]
    except (FileNotFoundError, ValueError):
        return []
