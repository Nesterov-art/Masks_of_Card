import os
from src.decorators import log
from datetime import datetime


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# Тест для логирования в консоль
def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b
    add(2, 3)
    captured = capsys.readouterr()
    output = captured.out
    assert "Вызов функции add с аргументами: args=(2, 3), kwargs={}" in output
    assert "Функция add завершилась успешно. Результат: 5" in output

# Тест для логирования в файл
def test_log_to_file(tmpdir):
    log_file = tmpdir.join("test_log.txt")

    @log(filename=str(log_file))
    def multiply(a, b):
        return a * b
    multiply(4, 5)
    log_content = read_file(str(log_file))
    assert "Вызов функции multiply с аргументами: args=(4, 5), kwargs={}" in log_content
    assert "Функция multiply завершилась успешно. Результат: 20" in log_content

# Тест для логирования ошибок
def test_log_error(tmpdir):
    log_file = tmpdir.join("error_log.txt")

    @log(filename=str(log_file))
    def divide(a, b):
        return a / b
    divide(10, 0)
    log_content = read_file(str(log_file))
    assert "Вызов функции divide с аргументами: args=(10, 0), kwargs={}" in log_content
    assert "Функция divide завершилась с ошибкой: division by zero" in log_content