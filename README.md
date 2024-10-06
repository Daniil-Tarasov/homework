# Виджет банковских операций клиента

## Описание

Виджет банковских операций - проект, разрабатываемый в процессе обучения по курсу "Разработчик на Python".
Это мой первый проект, который ещё будет наращивать свою функциональность.

## Установка

Клонируйте репозиторий:

```
git clone git@github.com:Daniil-Tarasov/homework.git
```

## Использование

1. Откройте скопированный проект.
2. Используйте модуль "widget", если вам необходимо замаскировать номер карты или счёта и для получения даты в формате дд.мм.гггг.
3. Используйте модуль "processing", если вам необходимо найти данные об операции по его статусу или его отсортировать данные по дате.
4. Используйте модуль "generators", если вам необходимо вывести поочерёдно транзакции с заданной валютой или вывести описание операции или сгенерировать номер карты по диапазону.

- При использовании модуля "widget" используйте команды:

Для маскировки номера карты или счёта:

```
pirnt(mask_account_card("выша_карта_или_счёт"))
```
Для получения даты операции:

```
print(get_date(дата_операции))
```
- При использовании модуля "processing" используйте команды:

Если вам необходимо найти данные об операции по его статусу:

```
print(filter_by_state(список_ваших_операций, статус)
```
Для сортировки по дате:
```
print(sort_by_date(список_ваших_операций, True по убыванию/False - по возрастанию)
```

- При использовании модуля "generators" используйте команды:

Для вывода транзакция с заданной волютой:

```
usd_transactions = filter_by_currency(список_транзакций, "валюта")
for _ in range(количество_выведенных_транзакций):
```
Для получения описания операции:

```
descriptions = transaction_descriptions(список_транзакций)
for _ in range(количество__выведенных_операций):
```
Для генерации номеров банковских карт:

```
for card_number in card_number_generator(диапзаон от 1 до 9999999999999999 через запятую):
    print(card_number)
```
## Тестирование

Для каждой функции из каждого модуля были проведены следующие тесты:

1. Модуль masks:
    - Функция ```get_mask_card_number```
      - Тестирование правильности маскирования номера карты.
      - Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
      - Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
    - Функция ```get_mask_account```
      - Тестирование правильности маскирования номера счета.
      - Проверка работы функции с различными форматами и длинами номеров счетов.
      - Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины.
      - Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер счёта.
2. Модуль widget:
   - Функция ```mask_account_card```
     - Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
     - Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
     - Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер и/или тип операции.
   - Функция ```get_data```
     - Тестирование правильности преобразования даты.
     - Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
     - Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
3. Модуль processing:
   - Функция ```filter_by_state```
     - Тестирование фильтрации списка словарей по заданному статусу state.
     - Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
   - Функция ```sort_by_date```
     - Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
     - Тесты на работу функции с некорректными или нестандартными форматами дат.
4. Модуль generators
   - Функция ```filter_by_currency```
     - Тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
     - Тестирование случаев, когда транзакции в заданной валюте отсутствуют.
     - Проверка на пустые входные данные
   - Функция ```transaction_descriptions```
     - Тесты, проверяющие корректность описаний.
     - Тесты с различным количеством входных данных
   - Функция ```card_number_generator```
     - Проверка правильности номеров карт
     - Проверка корректности форматирования