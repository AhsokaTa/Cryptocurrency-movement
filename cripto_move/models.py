import requests

class ModelError(Exception):
    pass

class CoinApiIO:
    def __init__(self):
        self.cryptocurrency_list = ["EUR","ETH","BNB","ADA","DOT","BTC","USDT","XRP","SOL","MATIC"]
        self.crypto_list=[]
    
    def GetCryptocurrencies(self, API_key):

        response=requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_key}')
        #if status code !=200, error
        if response.status_code != 200:
            raise Exception("Error response code")
        
        full_list = response.json()

        for item in full_list:
            if item["asset_id"] in self.cryptocurrency_list:
                self.crypto_list.append(item["asset_id"])

