import json


def get_data_about_financial_transactions(path_to_the_file):
    """Функция, которая возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_to_the_file, encoding="utf-8") as file:
            json.load(file)
    except ValueError:
        return []
    except FileNotFoundError:
        return []
    else:
        with open(path_to_the_file, encoding="utf-8") as file:
            operations = json.load(file)
            if type(operations) != list:
                return []
            else:
                return operations
