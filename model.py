import requests
# https://api.coinranking.com/v1/public/coin/1

def get_coin(id):
    response = requests.get('https://api.coinranking.com/v1/public/coin/' + str(id)).json()
    return response


