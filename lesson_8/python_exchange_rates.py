import requests
import datetime
from pprint import pprint as pp
import json
URL = 'https://api.exchangerate.host/convert'


def symbols():
    with open('symbols.json', 'r') as file:
        symbols_file = json.load(file)
    return symbols_file


symbols_file = symbols()


# выдаёт ошибку
# if currency_from == '' or currency_from not in symbols_file['symbols']:
# NameError: name 'symbols_file' is not defined


def values():
    currency_from = input('Convert from: ')
    if currency_from == '' or currency_from not in symbols_file['symbols']:
        currency_from = 'USD'
    currency_to = input('Convert to: ')
    if currency_to == '' or currency_to not in symbols_file['symbols']:
        currency_to = 'UAH'
    amount = float(input('Enter amount: '))
    if amount == 0.0:
        amount = 100.00
    pd = input("Please enter present day in format '%Y-%m-%d': ")
    start_date = datetime.datetime.strptime(pd, '%Y-%m-%d')
    if start_date != datetime.datetime.now():
        start_date = datetime.datetime.now() - datetime.timedelta(days=4)
    return convert(currency_from, currency_to, amount, start_date)


def convert(currency_from, currency_to, amount, start_date):
    result = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    while start_date <= datetime.datetime.now():
        request = requests.get('https://api.exchangerate.host/convert?',
                               params={'from': currency_from, 'to': currency_to, 'amount': amount, 'date': start_date})
        data = request.json()
        result.append([data['date'],
                       data['query']['from'],
                       data['query']['to'],
                       data['query']['amount'],
                       data['info']['rate'],
                       data['result']])
        start_date += datetime.timedelta(days=1)
    pp(result)


values()

if __name__ == 'python_exchange_rates':
    import argparse
    arguments = argparse.ArgumentParser()
    arguments.add_argument('from')
    arguments.add_argument('to')
    arguments.add_argument('amount')
    args = arguments.parse_args()
