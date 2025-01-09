from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(input_string: str):
    """ Маскирование номера счета или карты в зависимости от его типа """
    parts = input_string.split()
    if len(parts) < 2:
        return "Ошибка ввода: строка должна содержать тип и номер карты/счета."
    # Определяем тип карты или счета
    account_type = parts[0].lower()
    number = parts[-1].strip()
    # Маскируем в зависимости от типа
    if account_type in ["visa", "maestro"]:  # Если карта
        return get_mask_card_number(number)
    elif account_type == "счет":  # Если счет
        return get_mask_account(number)
    else:
        return "Ошибка ввода: неизвестный тип карты или счета."


def get_date(input_string: str):
    """ Получение текущей даты и времени """
    from datetime import datetime

    try:
        date_obj = datetime.strptime(input_string.strip(), "%d.%m.%Y")
        # Преобразуем обратно в нужный формат
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка ввода: дата должна быть в формате ДД.ММ.ГГГГ."


if __name__ == "__main__":
    print(get_date("12.12.2025"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 874305"))
