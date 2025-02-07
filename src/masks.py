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
