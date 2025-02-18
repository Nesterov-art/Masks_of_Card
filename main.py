from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.decorators import log
from src.utils import load_transactions
from src.external_api import convert_to_rub


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

