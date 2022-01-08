import requests
from data_manipulation import ast_agent

def login(auth_fact:str):
    url = "https://api.nobitex.ir/auth/login/"
    payload={'username': 'saeedjefe@gmail.com',
    'password': '860160Nobitex25400',
    'remember': 'yes',
    'captcha': 'api',
    'useragent': 'TraderBot/your_bot'}
    files=[

        ]   
    headers = {
        'X-TOTP': auth_fact
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response;

def get_exachange_info(coin:str):
    url = "https://api.nobitex.ir/v2/orderbook/" + coin
    payload = {}
    files = {}
    header= {}
    response = requests.request('GET', url, data = payload, files = files, headers=header);
    return response;


def get_balance(coin: str):

    url = "https://api.nobitex.ir/users/wallets/balance"+coin
    payload={'currency': coin }
    files=[

    ]
    
    headers = {
      'Authorization': 'Token '+ '8b74b6b03a2a6b0760a47845e991342cbb048645'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

    
def get_market_stats(coin: str):

    url = "https://api.nobitex.ir/market/stats"
    payload={'srcCurrency': coin,
    'dstCurrency': 'usdt,rls'}
    files=[

    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)




    
