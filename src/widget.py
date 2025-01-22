from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(input_string: str):
    """ Маскирование номера счета или карты в зависимости от его типа """
    parts = input_string.split()
    if len(parts) < 2:
        return "Ошибка ввода: строка должна содержать тип и номер карты/счета."
    # Определяем тип карты или счета
    account_type = parts[0].lower()
    number = parts[-1].strip()
    if account_type in ["visa", "maestro"]:  # Если карта
        return get_mask_card_number(number)
    elif account_type == "счет":  # Если счет
        return get_mask_account(number)
    else:
        return "Ошибка: неизвестный тип карты или счета."


def get_date(input_string: str):
    """ Получение текущей даты и времени """
    from datetime import datetime

    try:
        date_obj = datetime.strptime(input_string.strip(), "%d.%m.%Y")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка ввода: дата должна быть в формате ДД.ММ.ГГГГ."


