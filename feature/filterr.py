def filter_and_sort_transactions(transactions, state='EXECUTED', ascending=True):
    """
    Функция фильтрует список банковских операций по состоянию и сортирует их по дате
    """
    filtered_transactions = [transaction for transaction in transactions if transaction.get('state') == state]
    return sorted(filtered_transactions, key=lambda x: x.get('date'), reverse=not ascending)


transactions = [
    {"id": 1, "amount": 100, "state": "EXECUTED", "date": "2023-01-01"},
    {"id": 2, "amount": 200, "state": "PENDING", "date": "2023-01-02"},
    {"id": 3, "amount": 150, "state": "EXECUTED", "date": "2023-01-03"},
    {"id": 4, "amount": 50, "state": "FAILED", "date": "2023-01-04"}
]

state_to_filter = "EXECUTED"
filtered_and_sorted_transactions = filter_and_sort_transactions(transactions, state_to_filter)
print(filtered_and_sorted_transactions)