import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url)
# print(response.content)

name = url.split(".")[1].capitalize()
x = r.json()
for k, v in x.items():
    if k == "bpi":
        for x, y in v.items():
            if x == "USD":
                rate = y["rate_float"]
print(name, rate)


url1 = "https://api.coingecko.com/api/v3/exchange_rates"
r1 = requests.get(url1)
# print(response.content)

exchange_name = url1.split(".")[1].capitalize()
x1 = r1.json()
x1_rates = x1["rates"]
for k, v in x1_rates.items():
    if k == "usd":
        rate1 = v["value"]

print(exchange_name, rate1)


url2 = "https://api.coinbase.com/v2/prices/spot?currency=USD"
r2 = requests.get(url2)
# print(response.content)

exchange_name2 = url2.split(".")[1].capitalize()
x1 = r2.json()
rate2 = x1["data"]["amount"]

print(exchange_name2, rate2)

temp_dic = {name: rate, exchange_name: rate1, exchange_name2: float(rate2)}
higest = {}
lowest = {}
val1 = 0
val2 = 10000000
print(temp_dic)
for k, v in temp_dic.items():
    if v > val1:
        higest = {}
        higest[k] = v
        val1 = v
    if v < val2:
        lowest = {}
        lowest[k] = v
        val2 = v
print(lowest)
print(higest)

myDictObj = [
    {"All Exchanges USD price": temp_dic},
    {"Highest Priced Exchange": higest},
    {"Lowest Priced Exchange": lowest},
]

serialized = json.dumps(myDictObj, sort_keys=True, indent=3)
print(serialized)
