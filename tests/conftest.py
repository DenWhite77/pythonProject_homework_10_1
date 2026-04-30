import pytest


@pytest.fixture
def list_of_dicts():
    """Фикстура для тестов processing.py с разными статусами"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2024-01-02T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-03T10:00:00"},
        {"id": 4, "state": "CANCELED", "date": "2024-01-04T10:00:00"},
    ]


@pytest.fixture
def list_same_dates():
    """Фикстура с одинаковыми датами"""
    return [
        {"id": 1, "date": "2024-01-01T10:00:00"},
        {"id": 2, "date": "2024-01-01T10:00:00"},
    ]
