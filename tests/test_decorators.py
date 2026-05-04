"""
Тесты для модуля decorators.
"""

import os
import sys
from pathlib import Path

import pytest
from src.decorators import log

sys.path.append(str(Path(__file__).parent.parent))


# --- Тестовые функции ---

@log()
def add_success(a: int, b: int) -> int:
    """Успешная функция."""
    return a + b


@log()
def add_error(a: int, b: int) -> int:
    """Функция, бросающая ошибку."""
    raise ValueError("Тестовая ошибка")


@log()
def kwargs_success(**kwargs) -> str:
    """Функция с именованными аргументами."""
    return str(kwargs)


@log(filename="test_log.txt")
def multiply_success(a: int, b: int) -> int:
    """Успешная функция с логированием в файл."""
    return a * b


@log(filename="test_log.txt")
def multiply_error(a: int, b: int) -> int:
    """Функция с ошибкой и логированием в файл."""
    raise TypeError("Тестовая ошибка типа")


@log(filename="test_log.txt")
def divide_success(a: float, b: float) -> float:
    """Успешное деление с логированием в файл."""
    return a / b


# --- Тесты для консоли (capsys) ---

def test_log_success_console(capsys):
    """Тест логирования успешного вызова в консоль."""
    add_success(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "add_success ok"


def test_log_error_console(capsys):
    """Тест логирования вызова с ошибкой в консоль."""
    with pytest.raises(ValueError):
        add_error(1, 2)

    captured = capsys.readouterr()
    assert "add_error error: ValueError. Inputs: (1, 2), {}" in captured.out


def test_log_kwargs_console(capsys):
    """Тест логирования с именованными аргументами."""
    kwargs_success(a=1, b=2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "kwargs_success ok"


# --- Тесты для файла (tmp_path) ---

def test_log_success_file(tmp_path):
    """Тест логирования успешного вызова в файл."""
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        multiply_success(3, 4)
        with open("test_log.txt", 'r', encoding='utf-8') as f:
            content = f.read().strip()
        assert content == "multiply_success ok"
    finally:
        os.chdir(original_dir)


def test_log_error_file(tmp_path):
    """Тест логирования вызова с ошибкой в файл."""
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        with pytest.raises(TypeError):
            multiply_error(5, 'a')

        with open("test_log.txt", 'r', encoding='utf-8') as f:
            content = f.read().strip()
        expected = "multiply_error error: TypeError. Inputs: (5, 'a'), {}"
        assert expected in content
    finally:
        os.chdir(original_dir)


def test_log_multiple_calls_file(tmp_path):
    """Тест нескольких вызовов подряд — лог должен дописываться."""
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        multiply_success(2, 3)
        multiply_success(4, 5)
        with open("test_log.txt", 'r', encoding='utf-8') as f:
            lines = f.read().strip().split('\n')
        assert lines[0] == "multiply_success ok"
        assert lines[1] == "multiply_success ok"
        assert len(lines) == 2
    finally:
        os.chdir(original_dir)


def test_log_different_functions_file(tmp_path):
    """Тест записи в файл от разных функций."""
    original_dir = os.getcwd()
    os.chdir(tmp_path)
    try:
        multiply_success(2, 3)
        divide_success(10, 2)
        with open("test_log.txt", 'r', encoding='utf-8') as f:
            lines = f.read().strip().split('\n')
        assert lines[0] == "multiply_success ok"
        assert lines[1] == "divide_success ok"
    finally:
        os.chdir(original_dir)
