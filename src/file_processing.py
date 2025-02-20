import csv
import pandas as pd
import logging
from pathlib import Path

# Настройка логирования
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


def read_csv_transactions(file_path: str):
    """Считывание финансовых операций из CSV файла."""
    transactions = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                transactions.append(row)
        logger.info(f"Успешно считано {len(transactions)} транзакций из {file_path}")
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV {file_path}: {e}")
        return []
    return transactions


def read_excel_transactions(file_path: str):
    """Считывание финансовых операций из Excel файла."""
    transactions = []
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        logger.info(f"Успешно считано {len(transactions)} транзакций из {file_path}")
    except Exception as e:
        logger.error(f"Ошибка при чтении Excel {file_path}: {e}")
        return []
    return transactions
