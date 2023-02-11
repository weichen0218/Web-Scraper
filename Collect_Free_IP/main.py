import requests
import re

res = requests.get('https://free-proxy-list.net/')
all_ip = re.findall('\d+\.\d+\.\d+\.\d+:\d+', res.text)
valid_ip = []

for ip in all_ip:
    try:
        res = requests.get('https://api.ipify.org?format=json', proxies={'http': ip, 'https': ip}, timeout=5)
        valid_ip.append(ip)
        print(res.json())
    except:
        print('FAIL', ip)

path = 'output.txt'
with open(path, 'w') as f:
    for ip in valid_ip:
        f.write(f"{ip}\n")
