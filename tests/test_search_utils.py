from src.search_utils import search_transactions


def test_search_transactions_found():
    data = [{"description": "Перевод клиенту"}]
    result = search_transactions(data, "Перевод")
    assert len(result) == 1


def test_search_transactions_not_found():
    data = [{"description": "Оплата услуг"}]
    result = search_transactions(data, "Перевод")
    assert result == []


def test_search_transactions_empty():
    assert search_transactions([], "Перевод") == []
