import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_data_about_financial_transactions(path_to_the_file: str) -> list:
    """Функция, которая возвращает список словарей с данными о финансовых транзакциях"""
    try:

        with open(path_to_the_file, encoding="utf-8") as file:
            json.load(file)

    except ValueError as ex:
        logger.error(f"Произошла ошибка {ex}")

        return []

    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка {ex}")

        return []

    else:

        with open(path_to_the_file, encoding="utf-8") as file:
            operations = json.load(file)

            if type(operations) is not list:
                logger.info("Передан не список")

                return []

            else:
                logger.info("Успешное выполнение")

                return operations
