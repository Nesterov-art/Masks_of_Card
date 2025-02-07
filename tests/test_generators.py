import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            }
        },
        {
            "id": 2,
            "operationAmount": {
                "currency": {
                    "code": "EUR"
                }
            }
        },
        {
            "id": 3,
            "operationAmount": {
                "currency": {
                    "code": "USD"
                }
            }
        }
    ]


@pytest.fixture
def sample_transactions_with_descriptions():
    return [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
    ]


# Тесты filter_by_currency
@pytest.mark.parametrize("currency, expected_ids", [
    ("USD", [1, 3]),
    ("EUR", [2]),
    ("GBP", []),
])
def test_filter_by_currency(sample_transactions, currency, expected_ids):
    result = list(filter_by_currency(sample_transactions, currency))
    assert [t["id"] for t in result] == expected_ids


# Тесты transaction_descriptions
@pytest.mark.parametrize("index, expected_description", [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Перевод с карты на карту"),
])
def test_transaction_descriptions(sample_transactions_with_descriptions, index, expected_description):
    gen = transaction_descriptions(sample_transactions_with_descriptions)
    for _ in range(index + 1):
        description = next(gen)
    assert description == expected_description


# Тесты card_number_generator
@pytest.mark.parametrize("start, stop, expected_numbers", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    (0, 0, ["0000 0000 0000 0000"]),
])
def test_card_number_generator(start, stop, expected_numbers):
    gen = card_number_generator(start, stop)
    result = list(gen)
    assert result == expected_numbers

