from typing import Callable

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction_list: Callable) -> None:
    generator = filter_by_currency(transaction_list, "USD")
    assert next(generator) =={
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }


def test_transaction_descriptions(transaction_list: Callable) -> None:
    generator = transaction_descriptions([])
    assert next(generator) == None


@pytest.mark.parametrize(
    "start, stop, num_card",
    [
        (1, 5, "0000 0000 0000 0001"),
        (9999999999999997, 9999999999999999, "9999 9999 9999 9997")
    ]
)
def test_card_number_generator(start: int, stop: int, num_card: str) -> None:
    generator = card_number_generator(start, stop)
    assert next(generator) == num_card
