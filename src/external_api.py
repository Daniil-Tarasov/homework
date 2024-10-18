import os
from typing import Any

import requests
from dotenv import load_dotenv


def get_amount_in_rub(transaction: dict) -> Any:
    """Функция, которая конвертирует валюты из USD и EUR в рубли"""
    load_dotenv()
    api_key = os.getenv("API_KEY")
    amount = transaction["operationAmount"]["amount"]
    from_convert = transaction["operationAmount"]["currency"]["code"]
    to = "RUB"
    headers = {"apikey": api_key}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_convert}&amount={amount}"
    if from_convert == "RUB":

        return float(amount)

    else:
        response = requests.get(url, headers=headers)

        return response.json()["result"]
