import functools
from datetime import datetime


def log(filename=None):
    """
    Декоратор для логирования работы функции и её результата.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_message = (
                f"{datetime.now()} - Вызов функции {func.__name__} с аргументами: "
                f"args={args}, kwargs={kwargs}\n"
            )

            try:
                result = func(*args, **kwargs)
                log_message += f"{datetime.now()} - Функция {func.__name__} завершилась успешно. Результат: {result}\n"
            except Exception as e:
                log_message += f"{datetime.now()} - Функция {func.__name__} завершилась с ошибкой: {e}\n"
                result = None

            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_message)
            else:
                print(log_message, end="")

            return result

        return wrapper

    return decorator