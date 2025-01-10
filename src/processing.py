from datetime import datetime

def filter_by_state(operations, state='EXECUTED'):
    """
    Фильтрует список операций по значению ключа 'state'.
    """
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations, reverse=True):
    """
    Сортирует список операций по дате.
    """
    return sorted(
        operations,
        key=lambda op: datetime.strptime(op['date'], '%Y-%m-%d'),
        reverse=reverse
    )


operations = [
    {'state': 'EXECUTED', 'date': '2025-01-01', 'amount': 100},
    {'state': 'PENDING', 'date': '2025-01-02', 'amount': 200},
    {'state': 'EXECUTED', 'date': '2025-01-03', 'amount': 150},
    {'state': 'CANCELED', 'date': '2025-01-04', 'amount': 50},
]

executed_operations = filter_by_state(operations)
print("Фильтрованные операции:", executed_operations)
sorted_operations = sort_by_date(executed_operations)
print("Отсортированные операции:", sorted_operations)