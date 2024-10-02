from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    for i in transactions:
        if i["operationAmount"]["currency"]["name"] == currency:
            yield i


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    for i in transactions:
        yield i.get("description")


def card_number_generator(start: int, stop: int) -> Iterator:
    for num in range(start, stop):
        num_card = str(num)
        while len(num_card) < 16:
            num_card = "0" + num_card
        full_num_card = f"{num_card[:4]} {num_card[4:8]} {num_card[8:12]} {num_card[12:16]}"
        yield full_num_card

