import json
import os


def load_transactions(file_path="data/operations.json"):
    """
    Загружает список финансовых транзакций из JSON-файла.
    """
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
