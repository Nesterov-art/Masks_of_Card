import csv
import json
import pandas as pd
import logging
from pathlib import Path


LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

log_file = LOGS_DIR / "file_processing.log"
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file, mode="w"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("file_processing")


def read_csv(file_path: str):
    """Считывает транзакции из CSV и возвращает список словарей."""
    transactions = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
        logger.info(f"Успешно считан CSV-файл: {file_path}")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV: {e}")
    return transactions


def read_excel(file_path: str):
    """Считывает транзакции из Excel и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считан Excel-файл: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel: {e}")
        return []

def read_json(file_path: str):
    """Считывает транзакции из JSON и возвращает список словарей."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        logger.info(f"Успешно считан JSON-файл: {file_path}")
        return data
    except Exception as e:
        logger.error(f"Ошибка при чтении JSON: {e}")
        return []