def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты"""
    if not card_number:
        return ""
    card_str = str(card_number)
    if len(card_str) == 0:
        return ""
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета (показывает только последние 4 цифры)"""
    if not account_number:
        return ""
    account_str = str(account_number)
    if len(account_str) == 0:
        return ""
    return f"**{account_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
