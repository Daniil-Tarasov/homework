import os
from dotenv import load_dotenv
import requests


def get_amount_in_rub(transaction):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    amount = transaction['operationAmount']['amount']
    from_convert = transaction['operationAmount']['currency']['code']
    to = 'RUB'
    headers = {
        'apikey': api_key
    }
    if from_convert == 'RUB':
        return amount
    elif from_convert == 'USD':
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_convert}&amount={amount}'
        response = requests.get(url, headers=headers)
        result = response.json()
        return result['result']
    elif from_convert == 'EUR':
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_convert}&amount={amount}'
        response = requests.get(url, headers=headers)
        result = response.json()
        return result['result']
