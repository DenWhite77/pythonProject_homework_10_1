"""
Тесты для модуля utils.
"""

import json
from unittest.mock import mock_open, patch

import pytest

from src.utils import read_json


def test_read_json_success(tmp_path):
    """Тест успешного чтения JSON-файла."""
    test_file = tmp_path / "data.json"
    expected = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(expected, f)

    result = read_json(str(test_file))
    assert result == expected


def test_read_json_empty_list(tmp_path):
    """Тест: JSON-файл с пустым списком."""
    test_file = tmp_path / "empty.json"

    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump([], f)

    result = read_json(str(test_file))
    assert result == []


def test_read_json_not_a_list(tmp_path):
    """Тест: JSON-файл содержит не список (словарь)."""
    test_file = tmp_path / "dict.json"

    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump({"key": "value"}, f)

    result = read_json(str(test_file))
    assert result == []


def test_read_json_file_not_found():
    """Тест: файл не найден."""
    result = read_json("non_existent_file.json")
    assert result == []


def test_read_json_invalid_json(tmp_path):
    """Тест: некорректный JSON."""
    test_file = tmp_path / "invalid.json"

    with open(test_file, 'w', encoding='utf-8') as f:
        f.write("this is not json")

    result = read_json(str(test_file))
    assert result == []
    