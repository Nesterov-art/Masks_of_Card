from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
from src.utils import load_transactions
from src.external_api import convert_to_rub
from src.file_processing import read_csv, read_excel, read_json
from src.transaction_utils import (
    filter_transactions_by_status,
    filter_transactions_by_description,
    count_transactions_by_category,
    filter_by_currency,
    sort_transactions_by_date,
)


card_number = input("Введите номер карты ").strip()
number_account = input("Введите номер счета ").strip()


transactions = load_transactions()
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {
#             "amount": "43318.34",
#             "currency": {
#                 "name": "RUB",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160"
#     }
# ]

usd_transactions = filter_by_currency(transactions, "USD")
descriptions = transaction_descriptions(transactions)

start = 1
end = 10

if __name__ == "__main__":
    print(get_date("12.12.2025"))
    print("Маска номера счета:", get_mask_account(number_account))
    print("Маска номера карты:", get_mask_card_number(card_number))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 874305"))

    # filter_by_currency
    print("Транзакции в USD:")
    usd_transactions = filter_by_currency(transactions, "USD")
    for transaction in usd_transactions:
        print(transaction)

    # transaction_descriptions
    print("\nОписания транзакций:")
    descriptions = transaction_descriptions(transactions)
    for _ in range(2):
        print(next(descriptions))

    # card_number_generator
    print("\nНомера карт:")
    card_numbers = card_number_generator(1, 5)
    for card_number in card_numbers:
        print(card_number)

    @log(filename="log.txt")
    def multiply(a, b):
        return a * b
    @log(filename="log.txt")
    def subtract(a, b):
        return a - b

    multiply(4, 5)
    subtract(10, 5)

    # utils and external_api
    if transactions:
        amount_rub = convert_to_rub(transactions[0])
        print(f"Сумма в рублях: {amount_rub}")


def get_file_choice():
    """Запрашивает у пользователя выбор файла."""
    while True:
        choice = input(
            "Выберите источник данных:\n1. JSON\n2. CSV\n3. XLSX\nВведите число: "
        )
        if choice in ("1", "2", "3"):
            return choice
        print("Ошибка: введите 1, 2 или 3.")


def get_status_choice():
    """Запрашивает у пользователя статус транзакций."""
    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}
    while True:
        status = input("Введите статус (EXECUTED, CANCELED, PENDING): ").upper()
        if status in valid_statuses:
            return status
        print(f'Статус "{status}" недоступен.')


def yes_no_input(prompt):
    """Запрашивает у пользователя ответ Да/Нет."""
    while True:
        answer = input(f"{prompt} (Да/Нет): ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Ошибка: введите Да или Нет.")


def main():
    """Главная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    file_choice = get_file_choice()
    file_paths = {"1": "data/transactions.json", "2": "data/transactions.csv", "3": "data/transactions.xlsx"}
    file_path = file_paths[file_choice]

    print(f"Для обработки выбран файл: {file_path.split('/')[-1]}")

    transactions = []
    if file_choice == "1":
        transactions = read_json(file_path)
    elif file_choice == "2":
        transactions = read_csv(file_path)
    elif file_choice == "3":
        transactions = read_excel(file_path)

    if not transactions:
        print("Ошибка: файл пуст или не удалось загрузить данные.")
        return

    # Фильтрация по статусу
    status = get_status_choice()
    transactions = filter_transactions_by_status(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}".')

    # Сортировка по дате
    if yes_no_input("Отсортировать операции по дате?"):
        ascending = yes_no_input("Отсортировать по возрастанию?")
        transactions = sort_transactions_by_date(transactions, ascending)

    # Фильтр по валюте
    if yes_no_input("Выводить только рублевые транзакции?"):
        transactions = filter_by_currency(transactions)

    # Фильтр по описанию
    if yes_no_input("Отфильтровать список транзакций по определенному слову в описании?"):
        keyword = input("Введите слово: ")
        transactions = filter_transactions_by_description(transactions, keyword)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...\n")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под условия фильтрации.")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for tx in transactions:
            print(f"{tx['date']} {tx['description']} \nСчет {tx['account']} \nСумма: {tx['amount']}\n")


if __name__ == "__main__":
    main()