import pytest
from unittest.mock import mock_open, patch
from src.utils import load_transactions


def test_load_transactions_valid():
    mock_data = '[{"id": 1, "amount": 100}]'
    with patch("builtins.open", mock_open(read_data=mock_data)), patch("os.path.exists", return_value=True):
        result = load_transactions("data/operations.json")
        assert result == [{"id": 1, "amount": 100}]


def test_load_transactions_invalid_format():
    with patch("builtins.open", mock_open(read_data='{}')):
        result = load_transactions("data/operations.json")
        assert result == []

def test_load_transactions_empty_file():
    with patch("builtins.open", mock_open(read_data='')):
        result = load_transactions("data/operations.json")
        assert result == []

def test_load_transactions_file_not_found():
    with patch("os.path.exists", return_value=False):
        result = load_transactions("data/operations.json")
        assert result == []
