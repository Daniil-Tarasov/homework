from typing import Iterable

def filter_by_state(list_dict: Iterable[list], state: str="EXECUTED") -> list:
    """Возвращает новый список по заданному ключу"""
    new_list = []
    for key in list_dict:
        if key.get("state") == state:
            new_list.append(key)
    return new_list
