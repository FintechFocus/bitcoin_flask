import requests
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

# https://api.coinranking.com/v1/public/coin/1

def get_coin(id):
    response = requests.get('https://api.coinranking.com/v1/public/coin/' + str(id)).json()
    return response


