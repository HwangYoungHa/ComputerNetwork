import requests

# request를 통해 api에 요청
params = {'param1': 'value1', 'param2': 'value'}
response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR', params=params)

# 요청한 data를 slicing
s = str(response.text)[7:15]

usd = float(s)

# 출력
print("USD :", usd)