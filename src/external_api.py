"""
Модуль для работы с внешним API конвертации валют.
"""

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_currency(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции из USD или EUR в рубли.

    Args:
        transaction: Словарь с данными о транзакции

    Returns:
        Сумма в рублях (float). Если транзакция в RUB или не удалось сконвертировать,
        возвращается исходная сумма.
    """
    try:
        operation = transaction.get("operationAmount", {})
        amount = float(operation.get("amount", 0))
        currency_code = operation.get("currency", {}).get("code", "")

        if currency_code == "RUB":
            return amount

        if currency_code not in ("USD", "EUR"):
            return amount

        api_key = os.getenv("EXCHANGE_API_KEY")
        if not api_key or api_key == "your_api_key_here":
            return amount

        headers = {"apikey": api_key}
        params = {"base": currency_code, "symbols": "RUB"}

        response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()
        rate = data.get("rates", {}).get("RUB")

        if rate:
            return round(amount * rate, 2)
        return amount

    except (KeyError, ValueError, requests.RequestException):
        return amount
