import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


page = requests.get("https://www.tgju.org")
soup = BeautifulSoup(page.content, 'html.parser')
box = soup.find(id="home-quickview-wrapper")

def getPrice(tag):
    bourse_box = soup.select('#main > div.home-quickview-wrapper > div.container > div > ul '+tag)

    for span in bourse_box[0].span.find_all('span'):
        return (span.get_text())

data = {}
data['currencies'] = []

print(getPrice('#l-bourse'))
print(getPrice('#l-ons'))
print(getPrice('#l-mesghal'))
print(getPrice('#l-geram18'))
print(getPrice('#l-irec_future'))
print(getPrice('#l-price_dollar_rl'))
print(getPrice('#l-price_eur'))
print(getPrice('#l-oil_brent'))
print(getPrice('#l-crypto-bitcoin'))
data['currencies'].append({
    'bourse': getPrice('#l-bourse'),
    'ons': getPrice('#l-ons'),
    'mes': getPrice('#l-mesghal'),
    'gr': getPrice('#l-geram18'),
    'coin': getPrice('#l-irec_future'),
    'dollar': getPrice('#l-price_dollar_rl'),
    'eur': getPrice('#l-price_eur'),
    'oil': getPrice('#l-oil_brent'),
    'bitcoin': getPrice('#l-crypto-bitcoin')
})

with open('currencies.json', 'w') as outfile:
    json.dump(data, outfile)




