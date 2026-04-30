def get_mask_card_number(card_number: int) -> str:
    """
    Принимает номер карты в виде числа и возвращает маску.

    Формат: XXXX XX** **** XXXX

    Пример:
    get_mask_card_number(7000792289606361)
    '7000 79** **** 6361'
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Принимает номер счета в виде числа и возвращает маску.

    Формат: **XXXX

    Пример:
    get_mask_account(73654108430135874305)
    '**4305'
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
