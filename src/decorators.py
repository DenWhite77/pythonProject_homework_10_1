"""
Модуль с декораторами для логирования вызовов функций.
"""

import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций.

    Args:
        filename: Имя файла для записи логов.
            Если не указан, логи выводятся в консоль.

    Returns:
        Декоратор, оборачивающий функцию.
    """

    def log_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = (f"{func.__name__} error: {type(e).__name__}. "
                               f"Inputs: {args}, {kwargs}")
                _write_log(log_message, filename)
                raise

        return wrapper

    return log_decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """Вспомогательная функция для записи лога в файл или вывода в консоль."""
    if filename:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(message + '\n')
    else:
        print(message)
