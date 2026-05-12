import logging
import os

# Создаём папку для логов, если её нет
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG)

file_handler_masks = logging.FileHandler(os.path.join(LOG_DIR, 'masks.log'), mode='w', encoding='utf-8')
file_handler_masks.setLevel(logging.DEBUG)

file_formatter_masks = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler_masks.setFormatter(file_formatter_masks)

logger_masks.addHandler(file_handler_masks)


def get_mask_card_number(card_number: str) -> str:
    logger_masks.debug(f"Попытка маскирования номера карты: {card_number}")

    if not card_number:
        logger_masks.error("Передана пустая строка")
        return ""

    card_str = str(card_number)
    if len(card_str) == 0:
        logger_masks.error("Номер карты пуст после преобразования в строку")
        return ""

    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    logger_masks.info(f"Номер карты успешно замаскирован: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    logger_masks.debug(f"Попытка маскирования номера счёта: {account_number}")

    if not account_number:
        logger_masks.error("Передана пустая строка")
        return ""

    account_str = str(account_number)
    if len(account_str) == 0:
        logger_masks.error("Номер счёта пуст после преобразования в строку")
        return ""

    masked = f"**{account_str[-4:]}"
    logger_masks.info(f"Номер счёта успешно замаскирован: {masked}")
    return masked
