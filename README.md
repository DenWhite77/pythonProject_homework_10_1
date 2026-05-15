# Проект домашнего задания 10.1

## Цель проекта
Разработка функций для фильтрации и сортировки банковских операций.

## Установка и запуск

1. Клонируйте репозиторий:

```
bash
```
git clone https://github.com/DenWhite77/pythonProject_homework_10_1.git

## Модули проекта

### Генераторы (generators.py)
Модуль содержит функции-генераторы для работы с транзакциями.

filter_by_currency(transactions, currency)
Генератор, возвращающий транзакции заданной валюты.

transaction_descriptions(transactions)
Генератор описаний транзакций.

card_number_generator(start, stop)
Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

### Декораторы (decorators.py)
Модуль содержит декоратор log для автоматического логирования вызовов функций.

@log(filename=None)
Логирует вызов функции в консоль или в файл.

Если filename не указан — вывод в консоль.

Если filename указан — запись в файл (дописывание в конец).

#### Формат лога при успехе:

text
func_name ok

#### Формат лога при ошибке:

text
func_name error: ValueError. Inputs: (10, 0), {}

#### Пример использования:

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

### Тестирование
Проект покрыт тестами с использованием pytest.

#### Запуск тестов
pytest tests/ -v

#### Покрытие кода тестами
pytest tests/ --cov=src --cov-report=term
coverage html

#### Результаты тестирования
Общее покрытие: 87%
Все тесты: 24/24 passed (старые) + 7/7 passed (декораторы)
Тесты для генераторов: 9/9 passed
Тесты для декораторов: 7/7 passed

#### Фикстуры: используются в tests/conftest.py и tests/test_decorators.py
Параметризация: используется в тестах

### Утилиты (utils.py и external_api.py)
Модули для работы с JSON-файлами и конвертации валют через внешнее API.

#### Чтение JSON-файла
Функция read_json(file_path) читает JSON-файл с банковскими операциями и возвращает список словарей. При ошибке, пустом файле или не-списке — возвращает пустой список.

from src.utils import read_json

transactions = read_json("data/operations.json")
print(len(transactions))

#### Конвертация валюты
Функция convert_currency(transaction) переводит сумму транзакции из USD или EUR в рубли по текущему курсу. Для RUB и других валют возвращает исходную сумму.

Курс получает от сервиса Exchange Rates Data API. API-ключ хранится в файле .env.

from src.external_api import convert_currency

usd_tx = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
rub_amount = convert_currency(usd_tx)
print(rub_amount)

#### Настройка API
Получите бесплатный API-ключ на apilayer.com
Создайте файл .env в корне проекта:

text
EXCHANGE_API_KEY=ваш_ключ
Пример заполнения — в файле .env.example.

### Маскировка (masks.py, widget.py)
Функции для маскирования номеров карт и счетов.

### Обработка (processing.py)
Функции для фильтрации и сортировки транзакций.

## Работа с файлами

Модуль `file_reader` предоставляет функции для чтения финансовых транзакций из разных форматов.

- `read_csv_transactions(file_path)` — чтение CSV-файла
- `read_excel_transactions(file_path)` — чтение Excel-файла

Обе функции возвращают список словарей с данными транзакций. В случае ошибки (файл не найден, пустой файл, ошибка парсинга) возвращается пустой список.

## Установка зависимостей

Убедитесь, что установлены необходимые библиотеки:
```bash
pip install pandas openpyxl pytest pytest-cv flake8 mypy isort
```

## Тестирование
Запуск тестов:
pytest tests/ -v

Покрытие кода:
pytest tests/ --cov=src --cov-report=term

## 🚀 Шаг 8. Коммит, пуш и PR

```bash
git add .
git commit -m "feat: add CSV and Excel file readers with tests"
git push origin feature/file-readers
```


