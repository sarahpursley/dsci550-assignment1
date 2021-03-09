from bs4 import BeautifulSoup
import json
import requests
import random

def select_user():
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',	
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.0; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/29.0 Mobile/15E148 Safari/605.1.15',
        'Mozilla/5.0 (iPad; CPU OS 11_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/29.0 Mobile/15E148 Safari/605.1.15',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
    ]
    return random.choice(user_agents)

def lookup_ip(IP):
    url = 'https://scamalytics.com/ip/'
    d = {}
    try:
        page = requests.get(
            url + IP,
            headers = {'User-Agent': select_user()}
        )
    except:
        print("Error")
    soup = BeautifulSoup(page.content, 'html.parser')
    for text in soup.find_all('pre'):
        if 'ip' in text.string:
            new_data = json.loads(text.string)
            if new_data['ip'] == IP:
                d['risk_score'] = new_data['score']
                d['risk'] = new_data['risk']
    return d

def write_json(data, filename='fraudulent_emails_update.json'): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)
        f.close()

with open('path/to/data', 'r') as f:
    data = json.load(f)

for item in data:
    if 'IPInfo-data' in item:
        temp = item['IPInfo-data']
        append_info = lookup_ip(temp['ip'])
        if append_info != {}:
            temp['risk_score'] = append_info['risk_score']
            temp['risk'] = append_info['risk']
            print(temp['ip'], append_info)

write_json(data)
f.close()