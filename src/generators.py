def filter_by_currency(transactions, currency):
    """
    Фильтрует транзакции по заданной валюте.
    """
    for transaction in transactions:
        if transaction.get('operationAmount', {}).get('currency', {}).get('code') == currency:
            yield transaction

def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание каждой транзакции по очереди.
    """
    for transaction in transactions:
        yield transaction.get('description', 'Описание отсутствует')


def card_number_generator(start, stop):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        formatted_card_number = ' '.join([card_number[i:i+4] for i in range(0, 16, 4)])
        yield formatted_card_number

