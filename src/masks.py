def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счёта"""
    return "**" + account_number[-4:]


if __name__ == '__main__':
    input_card_number = input()
    input_account_number = input()
    print(get_mask_card_number(input_card_number))
    print(get_mask_account(input_account_number))
