from typing import Iterable

def filter_by_state(info_about_operation: Iterable[list], state: str="EXECUTED") -> list:
    """Возвращает новый список по заданному ключу"""
    new_list = []
    for key in info_about_operation:
        if key.get("state") == state:
            new_list.append(key)
    return new_list


def sort_by_date(info_about_operation: Iterable[list], ascending: bool=True) -> list:
    """Возвращает отсортированный список по дате"""
    if ascending == True:
        new_sorted_list = sorted(info_about_operation, key=lambda date: date.get("date"), reverse=True)
    else:
        new_sorted_list = sorted(info_about_operation, key=lambda date: date.get("date"))
    return new_sorted_list
