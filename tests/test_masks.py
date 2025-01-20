import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def valid_card_number():
    return "1234567890123456"

@pytest.fixture
def invalid_card_numbers():
    return [
        "12345678",
        "12345678901234567890",
        "1234abcd5678efgh",
        "",
        None
    ]

@pytest.fixture
def valid_account_number():
    return "987654321"

@pytest.fixture
def invalid_account_numbers():
    return [
        "123",
        "abcd5678",
        "",
        None
    ]


def test_get_mask_card_number_valid(valid_card_number):
    result = get_mask_card_number(valid_card_number)
    assert result == "1234 56 **** 3456"

def test_get_mask_card_number_invalid(invalid_card_numbers):
    for card_number in invalid_card_numbers:
        result = get_mask_card_number(card_number)
        assert result == "Ошибка ввода"


def test_get_mask_account_valid(valid_account_number):
    result = get_mask_account(valid_account_number)
    assert result == "**4321"

def test_get_mask_account_invalid(invalid_account_numbers):
    for account_number in invalid_account_numbers:
        result = get_mask_account(account_number)
        assert result == "Ошибка ввода"

