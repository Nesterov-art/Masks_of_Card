import csv
import pandas as pd
import logging
from pathlib import Path


LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS_DIR / "file_reader.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def read_csv(file_path: str):
    """
    Считывает данные из CSV-файла и возвращает список словарей с транзакциями.
    """
    transactions = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
        logger.info(f"Успешно считан CSV-файл: {file_path}")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV-файла {file_path}: {e}")
        return None
    return transactions


def read_excel(file_path: str):
    """
    Считывает данные из Excel-файла и возвращает список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        transactions = df.to_dict(orient="records")
        logger.info(f"Успешно считан Excel-файл: {file_path}")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel-файла {file_path}: {e}")
        return None
