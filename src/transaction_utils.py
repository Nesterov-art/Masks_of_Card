import re
from collections import defaultdict
from collections import Counter


def filter_transactions_by_description(transactions, keyword):
    """Фильтрует транзакции по ключевому слову в описании."""
    pattern = re.compile(keyword, re.IGNORECASE)
    return [tx for tx in transactions if pattern.search(tx.get("description", ""))]


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


def count_transactions_by_category(transactions, categories):
    """Подсчитывает количество транзакций по переданным категориям."""
    category_counts = Counter()
    for tx in transactions:
        description = tx.get("description", "").lower()
        for category in categories:
            if re.search(rf"\b{category}\b", description, re.IGNORECASE):
                category_counts[category] += 1
                break  # Учитываем только первую найденную категорию
    return dict(category_counts)

