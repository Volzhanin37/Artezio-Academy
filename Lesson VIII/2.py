import requests


def currency_exchanger(sum, cur1, cur2):
    r = requests.get('https://api.exchangerate-api.com/v4/latest/' + cur1)
    return ((r.json()['rates'][cur2]) * sum)


print((currency_exchanger(2.0, 'USD', 'RUB')))
