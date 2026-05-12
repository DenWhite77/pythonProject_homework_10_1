"""Тесты для модуля utils."""

import json

from src.utils import read_json


def test_read_json_success(tmp_path):
    """Тест успешного чтения JSON-файла."""
    test_file = tmp_path / "data.json"
    expected = [{"id": 1, "amount": 100}]

    with open(test_file, 'w', encoding='utf-8') as f:
        json.dump(expected, f)

    result = read_json(str(test_file))
    assert result == expected


def test_read_json_file_not_found():
    """Тест: файл не найден."""
    result = read_json("non_existent.json")
    assert result == []
    