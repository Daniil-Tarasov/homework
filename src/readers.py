import pandas as pd


def get_data_from_csv(path_to_the_file: str) -> list:
    """Функция, которая возвращает данные о финансовых транзакциях из файла csv"""
    try:
        with open(path_to_the_file, encoding="utf-8") as file:
            pd.read_csv(file)

    except ValueError:

        return []

    except FileNotFoundError:

        return []

    else:

        with open(path_to_the_file, encoding="utf-8") as file:
            operations = pd.read_csv(file, delimiter=";")
            return operations.to_dict(orient="records")


def get_data_from_excel(path_to_the_file: str) -> list:
    """Функция, которая возвращает данные о финансовых транзакциях из файла excel"""
    try:
        pd.read_excel(path_to_the_file)

    except ValueError:

        return []

    except FileNotFoundError:

        return []

    else:
        operations = pd.read_excel(path_to_the_file)
        return operations.to_dict(orient="records")
