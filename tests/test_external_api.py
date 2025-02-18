import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


def test_convert_usd_to_rub():
    with patch("src.external_api.get_exchange_rate", return_value=75.0):
        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
        result = convert_to_rub(transaction)
        assert result == 7500.0

def test_convert_eur_to_rub():
    with patch("src.external_api.get_exchange_rate", return_value=90.0):
        transaction = {"operationAmount": {"amount": "50", "currency": {"code": "EUR"}}}
        result = convert_to_rub(transaction)
        assert result == 4500.0

def test_convert_rub_to_rub():
    transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
    result = convert_to_rub(transaction)
    assert result == 1000.0

def test_convert_with_api_failure():
    with patch("src.external_api.get_exchange_rate", return_value=None):
        transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
        result = convert_to_rub(transaction)
        assert result is None