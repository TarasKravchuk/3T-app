import requests
import json
from app_3t.core.currency.date import *

def currency (currency):
    url_nbu_currency = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date='+date()+'&json'
    response = requests.get(url_nbu_currency)
    rate = json.loads(response.text)
    for element in rate:
        for key in element:
            if element.get(key) == 'USD':
                usd_dict = element
            elif element.get(key) == 'EUR':
                eur_dict = element

    if currency.upper() == 'USD':
        return float(usd_dict.get('rate'))
    elif currency.upper() == "EUR":
        return float(eur_dict.get('rate'))

def uah(var):
    uah_currency = var
    usd_currency = var / currency("USD")
    eur_currency = var / currency("EUR")
    return [uah_currency, usd_currency, eur_currency]

def eur(var):
    eur_currency = var
    uah_currency = var / currency("EUR")
    usd_currency = var * (currency("USD")/currency("EUR"))
    return  [uah_currency, usd_currency, eur_currency]

def usd (var):
    usd_currency = var
    uah_currency = var / currency("USD")
    eur_currency = var * (currency("EUR")/currency("USD"))
    return [uah_currency, usd_currency, eur_currency]
