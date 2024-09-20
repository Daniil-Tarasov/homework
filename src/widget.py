def mask_account_card(card_or_account: str) -> str:
    """Возвращает строку с замаскированным номером"""
    card_or_account_number = ""
    for numbers in card_or_account:
        if numbers.isdigit():
            card_or_account_number += numbers
    if len(card_or_account_number) == 16:
        return (f"{
        card_or_account_number[:4]} "
                f"{card_or_account_number[4:6]}** "
                f"**** {card_or_account_number[-4:]}")
    else:
        return "**" + card_or_account_number[-4:]


def get_date(full_date: str) -> str:
    """Возвращает дату в формате дд.мм.гггг"""
    pass


if __name__ == '__main__':
    card_or_account = input()
    print(mask_account_card(card_or_account))
