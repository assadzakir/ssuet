import requests

#Calculates the current price for currency (symbol) in comparison to USD or any provided currency
def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data

#print("The current price of BTC in USD=", price('BTC'))
#print("The current price of ETH in USD=", price('ETH'))