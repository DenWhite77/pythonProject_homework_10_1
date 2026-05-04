import sys
from pathlib import Path

# Добавляем корневую папку проекта в путь поиска модулей
sys.path.append(str(Path(__file__).parent.parent))


from src.processing import filter_by_state, sort_by_date

def test_filter_by_state():
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    executed = filter_by_state(data)
    print("Фильтрация по 'EXECUTED':")
    print(executed)

    canceled = filter_by_state(data, 'CANCELED')
    print("\nФильтрация по 'CANCELED':")
    print(canceled)

def test_sort_by_date():
    data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

    sorted_data = sort_by_date(data)
    print("\nСортировка по дате (по убыванию):")
    print(sorted_data)

if __name__ == "__main__":
    test_filter_by_state()
    test_sort_by_date()
