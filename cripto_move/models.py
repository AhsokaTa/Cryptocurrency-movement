import requests

class ModelError(Exception):
    pass

class CoinApiIO:
    def __init__(self,crypto_list):
        self.cryptocurrency_list = crypto_list
        self.crypto_list = []
    
    def getCryptocurrencies(self, API_key):

        response=requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_key}')
        #if status code !=200, error
        if response.status_code != 200:
            raise Exception("Error response code")        
        full_list = []
        full_list = response.json()
        for item in full_list:
            if item["asset_id"] in self.cryptocurrency_list:
                self.crypto_list.append(item["asset_id"])
    
    def crytocurrenciesValue(self, cryptocurrencie,API_key):
        response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{cryptocurrencie}/EUR?apikey={API_key}')
        if response.status_code != 200:
            raise Exception("Error response code")
        my_crypto = response.json()
        rate = my_crypto["rate"]        
        return rate
    
    def tradeoCrypto(self, q ,crypto_fom, crypto_to, API_key):
        q = float(q)  
        response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{crypto_fom}/{crypto_to}?apikey={API_key}')

        if response.status_code != 200:
            raise Exception("Error response code")
        r = response.json()
        rate = r["rate"]
        rate = float(rate)
        cambio = q/rate  

        return cambio
    

