import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_string, expected", [
    ("visa 1234567812345678", "1234 56 **** 5678"),
    ("счет 123456", "**3456"),
    ("maestro 1234567812345678", "1234 56 **** 5678"),
    ("visa", "Ошибка ввода: строка должна содержать тип и номер карты/счета."),
    ("mastercard 1234567890123456", "Ошибка: неизвестный тип карты или счета."),
    ("", "Ошибка ввода: строка должна содержать тип и номер карты/счета.")
])
def test_mask_account_card(input_string, expected):
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize("input_string, expected", [
    ("01.01.2023", "01.01.2023"),
    ("32.01.2023", "Ошибка ввода: дата должна быть в формате ДД.ММ.ГГГГ."),
    ("2023-01-01", "Ошибка ввода: дата должна быть в формате ДД.ММ.ГГГГ."),
    ("", "Ошибка ввода: дата должна быть в формате ДД.ММ.ГГГГ.")
])
def test_get_date(input_string, expected):
    assert get_date(input_string) == expected
