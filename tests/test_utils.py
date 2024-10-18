from unittest.mock import patch, mock_open

from src.utils import get_data_about_financial_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_get_data_about_financial_transactions(mock_file):
    transactions = get_data_about_financial_transactions("data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]

@patch("builtins.open", new_callable=mock_open, read_data='')
def test_empty_file(mock_file):
    transactions = get_data_about_financial_transactions("data/operations.json")
    assert transactions == []

@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 100}')
def test_not_a_list(mock_file):
    transactions = get_data_about_financial_transactions("data/operations.json")
    assert transactions == []

@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    transactions = get_data_about_financial_transactions("data/operations.json")
    assert transactions == []
