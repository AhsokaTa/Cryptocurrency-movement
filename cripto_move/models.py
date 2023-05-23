import requests

class ModelError(Exception):
    pass

class CoinApiIO:
    def __init__(self,crypto_list):
        self.cryptocurrency_list = crypto_list
        self.crypto_list = ""
    
    def getCryptocurrencies(self, API_key):

        response=requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={API_key}')
        #if status code !=200, error
        if response.status_code != 200:
            raise Exception("Error response code")
        
        full_list = response.json()

        for item in full_list:
            if item["asset_id"] in self.cryptocurrency_list:
                self.crypto_list.append(item["asset_id"])
    
    def crytocurrenciesValue(self, cryptocurrencie):
        response = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{cryptocurrencie}/EUR?apikey=93D86494-DCE3-4077-A9F4-5C36C1D86E34')
        if response.status_code != 200:
            raise Exception("Error response code")
        my_crypto = response.json()
        rate = my_crypto["rate"]
        
        return rate
    

