import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    operations = [
        {'state': 'EXECUTED', 'date': '2025-01-01', 'amount': 100},
        {'state': 'PENDING', 'date': '2025-01-02', 'amount': 200},
    ]
    assert filter_by_state(operations, 'EXECUTED') == [
        {'state': 'EXECUTED', 'date': '2025-01-01', 'amount': 100}
    ]
    assert filter_by_state(operations, 'PENDING') == [
        {'state': 'PENDING', 'date': '2025-01-02', 'amount': 200}
    ]
    assert filter_by_state(operations, 'CANCELED') == []


def test_sort_by_date():
    operations = [
        {'state': 'EXECUTED', 'date': '2025-01-03', 'amount': 150},
        {'state': 'EXECUTED', 'date': '2025-01-01', 'amount': 100},
        {'state': 'EXECUTED', 'date': '2025-01-02', 'amount': 200},
    ]

    sorted_ops = sort_by_date(operations)
    assert sorted_ops[0]['date'] == '2025-01-03'
    assert sorted_ops[-1]['date'] == '2025-01-01'

    sorted_ops = sort_by_date(operations, reverse=False)
    assert sorted_ops[0]['date'] == '2025-01-01'
    assert sorted_ops[-1]['date'] == '2025-01-03'

    operations_with_invalid_date = [
        {'state': 'EXECUTED', 'date': '01-01-2025', 'amount': 100},
    ]
    with pytest.raises(ValueError):
        sort_by_date(operations_with_invalid_date)
