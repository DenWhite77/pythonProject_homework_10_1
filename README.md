# Проект домашнего задания 10.1

## Цель проекта
Разработка функций для фильтрации и сортировки банковских операций.

## Установка и запуск

1. Клонируйте репозиторий:

```
bash
```

git clone https://github.com/DenWhite77/pythonProject_homework_10_1.git
Модули проекта
Генераторы (generators.py)
Модуль содержит функции-генераторы для работы с транзакциями.

filter_by_currency(transactions, currency)
Генератор, возвращающий транзакции заданной валюты.

transaction_descriptions(transactions)
Генератор описаний транзакций.

card_number_generator(start, stop)
Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

Декораторы (decorators.py)
Модуль содержит декоратор log для автоматического логирования вызовов функций.

@log(filename=None)
Логирует вызов функции в консоль или в файл.

Если filename не указан — вывод в консоль.

Если filename указан — запись в файл (дописывание в конец).

Формат лога при успехе:

text
func_name ok
Формат лога при ошибке:

text
func_name error: ValueError. Inputs: (10, 0), {}
Пример использования:

python
from src.decorators import log

@log(filename="mylog.txt")
def divide(a, b):
    return a / b

divide(10, 2)  # в файл mylog.txt добавится: divide ok
Маскировка (masks.py, widget.py)
Функции для маскирования номеров карт и счетов.

Обработка (processing.py)
Функции для фильтрации и сортировки транзакций.

Тестирование
Проект покрыт тестами с использованием pytest.

Запуск тестов
bash
pytest tests/ -v
Покрытие кода тестами
bash
pytest tests/ --cov=src --cov-report=term
coverage html
Результаты тестирования
Общее покрытие: 87%

Все тесты: 24/24 passed (старые) + 7/7 passed (декораторы)

Тесты для генераторов: 9/9 passed

Тесты для декораторов: 7/7 passed

Фикстуры: используются в tests/conftest.py и tests/test_decorators.py

Параметризация: используется в тестах