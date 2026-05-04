"""Модуль для маскировки данных карт/счетов и работы с датой."""

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    # Проверка типа
    if not isinstance(card_or_account_info, str):
        raise TypeError(f"Ожидается строка, получено {type(card_or_account_info).__name__}")
    """
    Принимает строку с типом и номером карты или счета.
    Возвращает строку с замаскированным номером.

    Примеры:
    mask_account_card("Visa Platinum 7000792289606361") -> "Visa Platinum 7000 79** **** 6361"
    mask_account_card("Счет 73654108430135874305") -> "Счет **4305"

    Raises:
    TypeError: Если аргумент не является строкой
    """
    # Разделяем строку на части (тип/название и номер)
    parts = card_or_account_info.rsplit(' ', 1)
    name = parts[0]
    number = parts[1]

    # Если это счет
    if name.lower() == "счет":
        # Маскировка для счета: ** + последние 4 цифры
        masked_number = get_mask_account(number)
        return f"{name} {masked_number}"
    else:
        # Маскировка для карты: первые 6 цифр (XXXX XX), потом **, потом ****, потом последние 4
        masked_number = get_mask_card_number(number)
        return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в формате "2024-03-11T02:26:18.671407"
    Возвращает строку с датой в формате "ДД.ММ.ГГГГ"

    Пример:
    get_date("2024-03-11T02:26:18.671407") -> "11.03.2024"
    """
    try:
        # Берём первые 10 символов (ГГГГ-ММ-ДД)
        date_part = date_string[:10]
        # Разбиваем по дефису
        year, month, day = date_part.split('-')
        # Возвращаем в формате ДД.ММ.ГГГГ
        return f"{day}.{month}.{year}"
    except (ValueError, AttributeError, IndexError):
        return "Неверный формат"


if __name__ == "__main__":
    # Проверка mask_account_card
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))

    # Проверка get_date
    print(get_date("2024-03-11T02:26:18.671407"))
