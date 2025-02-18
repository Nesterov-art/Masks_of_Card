import logging
import os


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
log_file = os.path.join(LOG_DIR, "masks.log")
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number='1234567890123456'):
    """ Маска номера карты """
    if len(card_number) != 16 or not card_number.isdigit():
        return "Ошибка ввода"
    mask_card_number = card_number[:4] + " " + card_number[4:6] + " **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(number_account: str):
    """ Маска номера счета """
    if len(number_account) < 4 or not number_account.isdigit():
        return "Ошибка ввода"
    mask_account = "**" + number_account[-4:]
    return mask_account


