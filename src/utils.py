import json
import os
import logging


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
log_file = os.path.join(LOG_DIR, "utils.log")
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def example_function(data):
    """ Функция для логирования """
    if not isinstance(data, str):
        logger.error(f"Ошибка: Ожидалась строка, получено {type(data)}")
        return "Ошибка"

    logger.info(f"Функция успешно обработала данные: {data}")
    return data.upper()


def load_transactions(file_path="data/operations.json"):
    """ Загружает список финансовых транзакций из JSON-файла """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                return []

            return data
    except (json.JSONDecodeError, IOError):
        return []

