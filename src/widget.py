from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Возвращает строку с замаскированным номером"""
    card_or_account_number = ""
    for numbers in card_or_account:
        if numbers.isdigit():
            card_or_account_number += numbers
    if len(card_or_account_number) == 16:
        return get_mask_card_number(card_or_account_number)
    else:
        return get_mask_account(card_or_account_number)


def get_date(full_date: str) -> str:
    """Возвращает дату в формате дд.мм.гггг"""
    return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"
