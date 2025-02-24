import re
from collections import defaultdict

def filter_transactions_by_description(transactions, keyword):
    """Фильтрует транзакции по ключевому слову в описании."""
    pattern = re.compile(keyword, re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx.get("description", ""))]


def count_transactions_by_category(transactions):
    """Подсчитывает количество транзакций по категориям (поле `description`)."""
    category_counts = defaultdict(int)
    for tx in transactions:
        category_counts[tx.get("description", "Неизвестная категория")] += 1
    return dict(category_counts)


def filter_transactions_by_status(transactions, status):
    """Фильтрует транзакции по статусу (без учета регистра)."""
    status = status.strip().upper()
    return [tx for tx in transactions if tx.get("status", "").upper() == status]


def filter_by_currency(transactions, currency="руб."):
    """Фильтрует транзакции, оставляя только рублевые."""
    return [tx for tx in transactions if currency in tx.get("amount", "")]


def sort_transactions_by_date(transactions, ascending=True):
    """Сортирует транзакции по дате."""
    return sorted(transactions, key=lambda tx: tx.get("date", ""), reverse=not ascending)
