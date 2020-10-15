import json

data_path = "../digital_currencies.json"

with open(data_path) as json_file:
        data = json.load(json_file)
        for p in data['digital_currencies']:
            if("BTC" in p['asset']):
               print(p)