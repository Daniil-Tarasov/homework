import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_or_account, type_and_mask_number",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Momentum 123456789101112131", "Momentum 1234 56** **** 2131"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", " ** **** "),
        ("Счет ", "Счет **"),
        ("Счет", "Счет ** **** "),
        ("73654108430135874305", "7365 41** **** 4305"),
    ],
)
def test_mask_account_card(card_or_account, type_and_mask_number):
    assert mask_account_card(card_or_account) == type_and_mask_number


def test_get_date(empty_date):
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

    assert get_date("2005-08-09") == "09.08.2005"

    assert get_date("2005-08") == ".08.2005"

    assert get_date("") == empty_date
