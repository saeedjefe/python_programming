import requests
from data_manipulation import ast_agent
import ast
from database_connector import send_to_mysql
import mysql.connector



def login(auth_fact:str, username:str, password:str):
    url = "https://api.nobitex.ir/auth/login/"
    payload={'username': username,
    'password': password,
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

def get_wallet_list():

    url = "https://api.nobitex.ir/users/wallets/list"
    payload={}
    headers = {
      'Authorization': 'Token 1cf472c5c39de6fc75e70d8a8190849b0ef37883'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_exachange_info(coin:str):
    url = "https://api.nobitex.ir/v2/orderbook/" 
    payload = {}
    files = {}
    header= {}
    response = requests.request('GET', url, data = payload, files = files, headers=header);
    return response;


def get_balance():

    headers = {
      'Authorization': 'Token '+ '1cf472c5c39de6fc75e70d8a8190849b0ef37883'
    }
    asset_and_balance_dic = dict();
    assets = set();
    assets = ('rls','dot','aave','bnb','etc','doge','eth','ada','btc','usdt','trx','shib','bch','xlm','ltc','xrp','eos', 'pmn','uni','dai','link');
    url = "https://api.nobitex.ir/users/wallets/balance"
    
    
    for asset in assets:
        value = "";
        payload={'currency': asset }
        files=[
            ]
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        dic = ast.literal_eval(response.text)
        for key in dic:
            if key == 'balance':
                value = dic[key];
                stms = send_to_mysql(asset, value);
                stms.sql_insertion(); 
     

    
def get_market_stats(coin: str):

    url = "https://api.nobitex.ir/market/stats"
    payload={'srcCurrency': coin,
    'dstCurrency': 'usdt,rls'}
    files=[

    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)




    
