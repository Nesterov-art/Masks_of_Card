import requests


def get_exchange_rate(currency_code):
    """
    Получает текущий курс валюты к рублю через API Exchange Rates Data.
    """
    API_KEY = "x6saMiG4BaQDrtcnM7f2aMiJbnwTfHVz"
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency_code}&symbols=RUB"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["rates"].get("RUB")
    except (requests.RequestException, KeyError, TypeError):
        return None


def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли, если она в другой валюте.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount

    exchange_rate = get_exchange_rate(currency_code)
    if exchange_rate:
        return round(amount * exchange_rate, 2)

    return None