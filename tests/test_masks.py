import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def valid_card_numbers():
    return [
        "1234567890123456",
        "9876543210987654",
        "0000000000000000",
        "1111222233334444"
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "12345",
        "12345678901234567",
        "",
        "123456789012345a",
        "12345678901234-6",
        "1234 5678 9012 3456",
        "12.34567890123456"
    ]


@pytest.fixture
def valid_accounts():
    return [
        "1234",
        "12345678901234567890",
        "98765432109876543210",
        "123456789012345678901234"
    ]


@pytest.fixture
def invalid_accounts():
    return [
        "123",
        "",
        "123a",
        "1234-5678",
        "1234 5678",
        "12.345"
    ]


@pytest.fixture
def expected_card_masks():
    return {
        "1234567890123456": "1234 56 **** 3456",
        "9876543210987654": "9876 54 **** 7654",
        "0000000000000000": "0000 00 **** 0000",
        "1111222233334444": "1111 22 **** 4444"
    }


@pytest.fixture
def expected_account_masks():
    return {
        "1234": "**1234",
        "12345678901234567890": "**7890",
        "98765432109876543210": "**3210",
        "123456789012345678901234": "**1234"
    }


@pytest.fixture
def card_format_checker():
    def _check_format(masked_number: str) -> bool:
        parts = masked_number.split(' ')
        if len(parts) != 4:
            return False
        if not (parts[0].isdigit() and len(parts[0]) == 4):
            return False
        if not (parts[1].isdigit() and len(parts[1]) == 2):
            return False
        if parts[2] != "****":
            return False
        if not (parts[3].isdigit() and len(parts[3]) == 4):
            return False
        return True
    return _check_format


@pytest.fixture
def account_format_checker():
    def _check_format(masked_number: str) -> bool:
        if not masked_number.startswith("**"):
            return False
        if not masked_number[2:].isdigit():
            return False
        return True
    return _check_format


def test_valid_cards(valid_card_numbers, expected_card_masks):
    for card_number in valid_card_numbers:
        expected = expected_card_masks[card_number]
        assert get_mask_card_number(card_number) == expected


def test_invalid_cards(invalid_card_numbers):
    for card_number in invalid_card_numbers:
        assert get_mask_card_number(card_number) == "Ошибка ввода"


def test_valid_accounts(valid_accounts, expected_account_masks):
    for account in valid_accounts:
        expected = expected_account_masks[account]
        assert get_mask_account(account) == expected


def test_invalid_accounts(invalid_accounts):
    for account in invalid_accounts:
        assert get_mask_account(account) == "Ошибка ввода"


def test_card_masking_format(valid_card_numbers, card_format_checker):
    for card_number in valid_card_numbers:
        masked = get_mask_card_number(card_number)
        assert card_format_checker(masked), f"Неверный формат маскирования: {masked}"


def test_account_masking_format(valid_accounts, account_format_checker):
    for account in valid_accounts:
        masked = get_mask_account(account)
        assert account_format_checker(masked), f"Неверный формат маскирования: {masked}"


def test_account_min_length():
    assert get_mask_account("1234") == "**1234"