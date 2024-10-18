import os
from dotenv import load_dotenv
from unittest.mock import patch

from src.external_api import get_amount_in_rub

@patch('requests.get')
def test_get_amount_in_rub(mock_convert):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    headers = {
        'apikey': api_key
    }
    mock_convert.return_value.json.return_value = {'result': 1.0}
    assert get_amount_in_rub({
        'operationAmount':
            {'amount': '1.0',
             'currency':
                  {'code': 'USD'}
              }
             }) == 1.0
    mock_convert.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1.0' ,headers=headers)
    assert get_amount_in_rub({
        'operationAmount':
            {'amount': '1.0',
             'currency':
                  {'code': 'RUB'}
              }
             }) == 1.0
    mock_convert.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1.0' ,headers=headers)

