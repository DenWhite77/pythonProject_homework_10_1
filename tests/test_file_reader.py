"""
Тесты для модуля file_reader.
"""

from unittest.mock import patch

import pandas as pd

from src.file_reader import read_csv_transactions, read_excel_transactions


@patch("pandas.read_csv")
def test_read_csv_success(mock_read_csv):
    mock_df = pd.DataFrame({'id': [1, 2], 'amount': [100, 200]})
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("fake.csv")
    expected = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]
    assert result == expected
    mock_read_csv.assert_called_once_with("fake.csv")


@patch("pandas.read_csv")
def test_read_csv_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError
    result = read_csv_transactions("missing.csv")
    assert result == []


@patch("pandas.read_csv")
def test_read_csv_empty_file(mock_read_csv):
    mock_read_csv.side_effect = pd.errors.EmptyDataError
    result = read_csv_transactions("empty.csv")
    assert result == []


@patch("pandas.read_csv")
def test_read_csv_parser_error(mock_read_csv):
    mock_read_csv.side_effect = pd.errors.ParserError
    result = read_csv_transactions("bad.csv")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_success(mock_read_excel):
    mock_df = pd.DataFrame({'id': [1, 2], 'amount': [100, 200]})
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake.xlsx")
    expected = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]
    assert result == expected
    mock_read_excel.assert_called_once_with("fake.xlsx", engine='openpyxl')


@patch("pandas.read_excel")
def test_read_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError
    result = read_excel_transactions("missing.xlsx")
    assert result == []


@patch("pandas.read_excel")
def test_read_excel_invalid_file(mock_read_excel):
    mock_read_excel.side_effect = ValueError
    result = read_excel_transactions("bad.xlsx")
    assert result == []
