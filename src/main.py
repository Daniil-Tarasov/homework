from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import get_data_from_csv, get_data_from_excel
from src.sorting import get_transactions_on_search_bar
from src.utils import get_data_about_financial_transactions
from src.widget import get_date, mask_account_card


def file_selection():
    user_input = input()
    if user_input == "1":
        print("Для обработки выбран JSON-файл.")
        return get_data_about_financial_transactions('../data/operations.json')
    elif user_input == "2":
        print("Для обработки выбран CSV-файл")
        return get_data_from_csv("../data/transactions.csv")
    elif user_input == '3':
        print("Для обработки выбран EXCEL-файл")
        return get_data_from_excel('../data/transactions_excel.xlsx')
    else:
        print("Введён некорректный номер")


def choice_state(data):
    while True:
        print('Введите статус, по которому необходимо выполнить фильтрацию.'
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        user_input_2 = input()
        if user_input_2 == "EXECUTED" or user_input_2 == "CANCELED" or user_input_2 == "PENDING":
            print(f'Операции отфильтрованы по статусу "{user_input_2}"')
            data = filter_by_state(data, user_input_2.upper())
            break
        else:
            print(f'Статус операции "{user_input_2}" недоступен')
    return data


def choice_sort_by_date(data):
    choice_sort = input()
    if choice_sort.lower() == 'да':
        print("Отсортировать по возрастанию или по убыванию?")
        sort_up_or_lower = input()
        if sort_up_or_lower.lower() == 'по возрастанию':
            is_reverse = False
            data = sort_by_date(data, is_reverse)
        else:
            is_reverse = True
            data = sort_by_date(data, is_reverse)
    return data


def sort_by_rub(data):
    rub_transaction = input()
    if rub_transaction.lower() == 'да':
        data = filter_by_currency(data, "RUB")
    return list(data)


def filter_by_world(data, sort_by_word):
    if sort_by_word.lower() == 'да':
        print('Введите слово:')
        string_to_search = input()
        data = get_transactions_on_search_bar(data, string_to_search)
    return data


def ending_result(data):
    if len(data) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(data)}\n")

        for transaction in data:
            date = get_date(transaction.get("date"))

            try:
                mask_from = mask_account_card(transaction["from"])
                print(f"{date} {transaction["description"]} {mask_from} -> ", end="")
            except KeyError:
                print(f"{date} {transaction["description"]} ", end="")
            except AttributeError:
                print(f"{date} {transaction["description"]} ", end="")

            mask_to = mask_account_card(transaction["to"])
            try:
                amount = transaction["amount"]
            except KeyError:
                amount = transaction["operationAmount"]["amount"]
            try:
                currency = transaction["currency_name"]
            except KeyError:
                currency = transaction["operationAmount"]["currency"]["name"]
            print(f"{mask_to} Сумма: {amount} {currency}")


def main():
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")
    data = file_selection()
    data = choice_state(data)
    print('Отсортировать операции по дате? Да/Нет')
    data = choice_sort_by_date(data)
    print("Выводить только рублевые транзакции? Да/Нет")
    data = sort_by_rub(data)
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_by_word = input()
    data = filter_by_world(data, sort_by_word)
    print('Распечатываю итоговый список транзакций...')
    ending_result(data)

if __name__ == '__main__':
    main()
