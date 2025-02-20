import pytest
import csv
import pandas as pd
from unittest.mock import mock_open, patch
from src.file_processing import read_csv_transactions, read_excel_transactions


# Тест для CSV-файла с Mock
@pytest.fixture
def sample_csv():
    return "date,amount,description\n2024-02-20,1000,Salary\n2024-02-21,-200,Dinner\n"


def test_read_csv_transactions(sample_csv):
    with patch("builtins.open", mock_open(read_data=sample_csv)) as mock_file:
        with patch("csv.DictReader", return_value=[{"date": "2024-02-20", "amount": "1000", "description": "Salary"},
                                                   {"date": "2024-02-21", "amount": "-200", "description": "Dinner"}]):
            result = read_csv_transactions("mock.csv")
            assert len(result) == 2
            assert result[0]["description"] == "Salary"
            assert result[1]["amount"] == "-200"
            mock_file.assert_called_once_with("mock.csv", newline='', encoding='utf-8')


# Тест для Excel-файла с Mock
@pytest.fixture
def sample_excel_data():
    return pd.DataFrame([
        {"date": "2024-02-20", "amount": 1000, "description": "Salary"},
        {"date": "2024-02-21", "amount": -200, "description": "Dinner"}
    ])


def test_read_excel_transactions(sample_excel_data):
    with patch("pandas.read_excel", return_value=sample_excel_data):
        result = read_excel_transactions("mock.xlsx")
        assert len(result) == 2
        assert result[0]["description"] == "Salary"
        assert result[1]["amount"] == -200
