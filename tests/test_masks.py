from collections.abc import Callable

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(empty_cards_numbers: Callable) -> None:
    assert get_mask_card_number("1234567891011121") == "1234 56** **** 1121"

    assert get_mask_card_number("123456789101112131") == "1234 56** **** 2131"

    assert get_mask_card_number("1234567891011121314") == "1234 56** **** 1314"

    assert get_mask_card_number("1234567891011") == "1234 56** **** 1011"

    assert get_mask_card_number("123456789101112") == "1234 56** **** 1112"

    assert get_mask_card_number("") == empty_cards_numbers


def test_get_mask_account(empty_accounts_numbers: Callable) -> None:
    assert get_mask_account("73654108430135874305") == "**4305"

    assert get_mask_account("736541084301358743059874562") == "**4562"

    assert get_mask_account("73654108430132") == "**0132"

    assert get_mask_account("") == empty_accounts_numbers
