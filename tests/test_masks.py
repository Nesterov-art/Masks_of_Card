import pytest

from unittest.mock import patch
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 **** **** 5678"),
    ("12345678", "Ошибка ввода"),
    ("123456781234567890", "Ошибка ввода"),
    ("1234abcd5678efgh", "Ошибка ввода"),
    ("", "Ошибка ввода"),
    (None, "Ошибка ввода"),
])
def test_get_card_number_valid():
    with patch('builtins.input', return_value='1234567890123456'):
        assert get_mask_card_number() == '1234567890123456'

def test_get_card_number_invalid_length():
    with patch('builtins.input', return_value='123'):
        assert get_mask_card_number() == 'Ошибка ввода'

def test_get_card_number_invalid_characters():
    with patch('builtins.input', return_value='1234abcd5678efgh'):
        assert get_mask_card_number() == 'Ошибка ввода'


@pytest.mark.parametrize("number_account, expected", [
    ("1234567890123456", "************3456"),
    ("123456", "123456"),
    ("123", "Ошибка ввода"),
    ("abcd5678", "Ошибка ввода"),
    ("", "Ошибка ввода"),
    (None, "Ошибка ввода"),
])
def test_get_mask_account(number_account, expected):
    assert get_mask_account(number_account) == expected

