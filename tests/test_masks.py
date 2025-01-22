import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def valid_card_numbers():
    """Фикстура с корректными номерами карт"""
    return [
        "1234567890123456",
        "9876543210987654",
        "0000000000000000",
        "1111222233334444"
    ]


@pytest.fixture
def invalid_card_numbers():
    """Фикстура с некорректными номерами карт"""
    return [
        "12345",  # короткий номер
        "12345678901234567",  # длинный номер
        "",  # пустая строка
        "123456789012345a",  # буквы
        "12345678901234-6",  # специальные символы
        "1234 5678 9012 3456",  # пробелы
        "12.34567890123456"  # точки
    ]


@pytest.fixture
def valid_accounts():
    """Фикстура с корректными номерами счетов"""
    return [
        "1234",  # минимальная длина
        "12345678901234567890",  # стандартный номер
        "98765432109876543210",  # другой стандартный номер
        "123456789012345678901234"  # длинный номер
    ]


@pytest.fixture
def invalid_accounts():
    """Фикстура с некорректными номерами счетов"""
    return [
        "123",  # слишком короткий
        "",  # пустой
        "123a",  # буквы
        "1234-5678",  # дефис
        "1234 5678",  # пробелы
        "12.345"  # точка
    ]


@pytest.fixture
def expected_card_masks():
    """Фикстура с ожидаемыми результатами маскирования карт"""
    return {
        "1234567890123456": "1234 56 **** 3456",
        "9876543210987654": "9876 54 **** 7654",
        "0000000000000000": "0000 00 **** 0000",
        "1111222233334444": "1111 22 **** 4444"
    }


@pytest.fixture
def expected_account_masks():
    """Фикстура с ожидаемыми результатами маскирования счетов"""
    return {
        "1234": "**1234",
        "12345678901234567890": "**7890",
        "98765432109876543210": "**3210",
        "123456789012345678901234": "**1234"
    }


@pytest.fixture
def card_format_checker():
    """Фикстура для проверки формата маскированного номера карты"""
    def _check_format(masked_number: str) -> bool:
        parts = masked_number.split(' ')
        if len(parts) != 4:  # должно быть 4 части
            return False
        if not (parts[0].isdigit() and len(parts[0]) == 4):  # первые 4 цифры
            return False
        if not (parts[1].isdigit() and len(parts[1]) == 2):  # следующие 2 цифры
            return False
        if parts[2] != "****":  # звездочки
            return False
        if not (parts[3].isdigit() and len(parts[3]) == 4):  # последние 4 цифры
            return False
        return True
    return _check_format


@pytest.fixture
def account_format_checker():
    """Фикстура для проверки формата маскированного номера счета"""
    def _check_format(masked_number: str) -> bool:
        if not masked_number.startswith("**"):
            return False
        if not masked_number[2:].isdigit():
            return False
        return True
    return _check_format


def test_valid_cards(valid_card_numbers, expected_card_masks):
    """Тест маскирования корректных номеров карт"""
    for card_number in valid_card_numbers:
        expected = expected_card_masks[card_number]
        assert get_mask_card_number(card_number) == expected


def test_invalid_cards(invalid_card_numbers):
    """Тест маскирования некорректных номеров карт"""
    for card_number in invalid_card_numbers:
        assert get_mask_card_number(card_number) == "Ошибка ввода"


def test_valid_accounts(valid_accounts, expected_account_masks):
    """Тест маскирования корректных номеров счетов"""
    for account in valid_accounts:
        expected = expected_account_masks[account]
        assert get_mask_account(account) == expected


def test_invalid_accounts(invalid_accounts):
    """Тест маскирования некорректных номеров счетов"""
    for account in invalid_accounts:
        assert get_mask_account(account) == "Ошибка ввода"


def test_card_masking_format(valid_card_numbers, card_format_checker):
    """Тест формата маскирования карт"""
    for card_number in valid_card_numbers:
        masked = get_mask_card_number(card_number)
        assert card_format_checker(masked), f"Неверный формат маскирования: {masked}"


def test_account_masking_format(valid_accounts, account_format_checker):
    """Тест формата маскирования счетов"""
    for account in valid_accounts:
        masked = get_mask_account(account)
        assert account_format_checker(masked), f"Неверный формат маскирования: {masked}"


def test_account_min_length():
    """Тест минимальной длины номера счета"""
    assert get_mask_account("1234") == "**1234"