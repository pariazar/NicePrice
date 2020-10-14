import requests
from bs4 import BeautifulSoup
import json
def main():
    listCurrencies = []
    #list of datas
    data = {}
    data['digital_currencies'] = []
    sep = 0

    headers = {'User-Agent': 'Mozilla/5.0'}
    y = ["gold-price","silver-price","platinum-price","palladium-price"]
    url = "https://www.coindesk.com/coindesk20"
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, 'html.parser')
    s4 = soup.select("#__next > div:nth-child(2) > main > section > div.data-module > div.cex-table-wrapper > div > section > section.tbody")
    for span in s4[0].findAll("section"):
            if(str(span.find("span")) != "None"):
                result = span
                rows = result.find_all('span')
                for x in rows:
                    listCurrencies.append(x.get_text())
                    sep += 1
                    if(sep>10):
                        data['digital_currencies'].append({
                        'asset': listCurrencies[2],
                        'price': listCurrencies[3],
                        'market cap': listCurrencies[4],
                        'total exchange volume': listCurrencies[5],
                        'returns 24h': listCurrencies[6],
                        'total supply': listCurrencies[7],
                        'category': listCurrencies[8],
                        'value proposition': listCurrencies[9]
                        })
                        listCurrencies = []
                        sep = 0
                    

    with open('./digital_currencies.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()