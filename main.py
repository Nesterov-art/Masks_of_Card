from src.masks import get_mask_card_number, get_mask_account
from src.widget import get_date, mask_account_card

card_number = input("Введите номер карты ").strip()
number_account = input("Введите номер счета ").strip()

if __name__ == "__main__":
    print(get_date("12.12.2025"))
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 874305"))
    print("Маска номера счета:", get_mask_account(number_account))
    print("Маска номера карты:", get_mask_card_number(card_number))
