from src.counter_utils import count_transactions_by_category


def test_count_categories():
    data = [{"description": "Перевод"}, {"description": "Перевод"}, {"description": "Оплата"}]
    result = count_transactions_by_category(data, ["Перевод", "Оплата"])
    assert result == {"Перевод": 2, "Оплата": 1}


def test_count_categories_empty():
    assert count_transactions_by_category([], ["Перевод"]) == {"Перевод": 0}
