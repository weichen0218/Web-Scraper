import requests
import re
import pandas
from bs4 import BeautifulSoup

dfs = pandas.read_html('https://rate.bot.com.tw/xrt?Lang=zh-TW')
df = dfs[0]
df = df.iloc[:, [0, 2]]
df.columns = ['coin', 'price']
df['coin'] = df['coin'].str.extract('.+\((.+)\)')

price_dic = {}
for idx, rec in df.iterrows():
    if rec.price != '-':
        price_dic[rec.coin] = float(rec.price)

country_code = {'us': 'USD', 'uk': 'GBP', 'tw': 'TWD', 'jp': 'JPY', 'kr': 'KRW'}
for country in country_code:
    res = requests.get(f'https://{country}.burberry.com/quilted-leather-small-lola-bag-p80630081')
    soup = BeautifulSoup(res.text, 'lxml')
    price_text = soup.select_one('.product-info-panel__price').text
    price = float(''.join([e for e in price_text if re.match('[0-9.]', e)]))
    print(country, price * price_dic.get(country_code.get(country), 1))
