import sys
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
sys.path.append(str(Path(__file__).parent.parent))

"""
Главный модуль проекта для работы с банковскими транзакциями.
"""

import os
from datetime import datetime
from typing import List, Dict, Any

from src.file_reader import read_csv_transactions, read_excel_transactions
from src.utils import read_json
from src.search_utils import search_transactions
from src.counter_utils import count_transactions_by_category


def filter_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """
    Фильтрует транзакции по статусу (регистронезависимо).

    Args:
        transactions: Список транзакций.
        status: Статус для фильтрации (например, 'EXECUTED').

    Returns:
        Отфильтрованный список транзакций.
    """
    status_upper = status.upper()
    result = []
    for t in transactions:
        state_value = t.get("state")
        if isinstance(state_value, str):
            if state_value.upper() == status_upper:
                result.append(t)
        # Если значение не строка — игнорируем такую транзакцию
    return result


def sort_by_date(transactions: List[Dict[str, Any]], ascending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует транзакции по дате.

    Args:
        transactions: Список транзакций.
        ascending: True — по возрастанию (старые сначала), False — по убыванию (новые сначала).

    Returns:
        Отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x.get("date", ""), reverse=not ascending)


def filter_rub_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Оставляет только рублевые транзакции.

    Args:
        transactions: Список транзакций.

    Returns:
        Список транзакций в рублях.
    """
    return [t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]


def format_transaction(transaction: Dict[str, Any]) -> str:
    """
    Форматирует одну транзакцию для красивого вывода.

    Args:
        transaction: Словарь с данными транзакции.

    Returns:
        Отформатированная строка с транзакцией.
    """
    date_str = transaction.get("date", "")[:10]
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d.%m.%Y")
    except ValueError:
        formatted_date = date_str

    description = transaction.get("description", "Нет описания")

    # Форматирование from и to
    from_info = transaction.get("from", "Неизвестно")
    to_info = transaction.get("to", "Неизвестно")

    # Форматирование суммы
    amount_info = transaction.get("operationAmount", {})
    amount = amount_info.get("amount", "0")
    currency = amount_info.get("currency", {}).get("code", "")

    # Простой вывод для примера
    return f"{formatted_date} {description}\n{from_info} -> {to_info}\nСумма: {amount} {currency}\n"


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    if choice == "1":
        file_path = "data/operations.json"
        transactions = read_json(file_path)
        if transactions:
            print("Пример транзакции:", transactions[0])
            print("Доступные статусы:", set(t.get("state", "") for t in transactions))
        else:
            print("Транзакции не загрузились или список пуст")
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = "data/transactions.csv"
        transactions = read_csv_transactions(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        transactions = read_excel_transactions(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции. Завершение программы.")
        return

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip()
        if status.upper() in valid_statuses:
            break
        print(f"Статус операции \"{status}\" недоступен.")

    filtered_by_status = filter_by_status(transactions, status)
    print(f"Операции отфильтрованы по статусу \"{status.upper()}\"")
    print(f"Найдено {len(filtered_by_status)} транзакций.")

    if not filtered_by_status:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Сортировка по дате
    print("\nОтсортировать операции по дате? Да/Нет")
    sort_choice = input().strip().lower()
    if sort_choice in ["да", "yes", "y"]:
        print("Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию)")
        order = input().strip().lower()
        ascending = order in ["по возрастанию", "возрастанию", "asc"]
        filtered_by_status = sort_by_date(filtered_by_status, ascending=ascending)

    # Фильтрация по рублевым транзакциям
    print("\nВыводить только рублевые транзакции? Да/Нет")
    rub_only = input().strip().lower()
    if rub_only in ["да", "yes", "y"]:
        filtered_by_status = filter_rub_transactions(filtered_by_status)
        print("Отфильтровано только рублевые транзакции.")

    if not filtered_by_status:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Поиск по описанию
    print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")
    search_choice = input().strip().lower()
    if search_choice in ["да", "yes", "y"]:
        print("Введите слово для поиска:")
        search_word = input().strip()
        filtered_by_status = search_transactions(filtered_by_status, search_word)

    if not filtered_by_status:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Подсчёт категорий (дополнительная функция)
    print("\nВведите категории для подсчёта (через запятую, например: Перевод, Покупка, Оплата):")
    categories_input = input().strip()
    if categories_input:
        categories = [cat.strip() for cat in categories_input.split(",") if cat.strip()]
        if categories:
            counts = count_transactions_by_category(filtered_by_status, categories)
            print("\nПодсчёт по категориям:")
            for cat, cnt in counts.items():
                print(f"{cat}: {cnt}")

    # Вывод итогового списка
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(filtered_by_status)}\n")

    for t in filtered_by_status:
        print(format_transaction(t))
        print("-" * 50)


if __name__ == "__main__":
    main()
