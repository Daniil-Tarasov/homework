import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    logger.info(f"Внесённые данные {card_number}")
    try:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    except TypeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return "Передана не строка"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счёта"""
    logger.info(f"Внесённые данные {account_number}")
    try:
        return "**" + account_number[-4:]
    except TypeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        return "Передана не строка"
