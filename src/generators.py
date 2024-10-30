from typing import Iterator


def filter_by_currency(info_about_transactions: list[dict], currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    if len(info_about_transactions) > 0:
        for i in info_about_transactions:
            try:
                if i["operationAmount"]["currency"]["code"] == currency:
                    yield i
            except KeyError:
                if i["currency_code"] == currency:
                    yield i


def transaction_descriptions(info_about_transactions: list[dict]) -> Iterator:
    """Возвращает описание каждой операции по очереди"""

    if len(info_about_transactions) > 0:
        for i in info_about_transactions:
            yield i.get("description")
    yield


def card_number_generator(start: int, stop: int) -> Iterator:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""

    for num in range(start, stop + 1):
        num_card = str(num)
        while len(num_card) < 16:
            num_card = "0" + num_card
        full_num_card = f"{num_card[:4]} {num_card[4:8]} {num_card[8:12]} {num_card[12:16]}"
        yield full_num_card
