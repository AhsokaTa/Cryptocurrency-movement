from cripto_move import app
from flask import render_template
import requests
from cripto_move.models import *
from cripto_move.database import *


@app.route("/")
def index():
    JSONstructure = [
    {
    "id": '1',
    "date": 'date field',
    "time": 'time field',
    "from": 'from field',
    "q": 'q field',
    "to": 'to field',
    "q1": 'q1 field',
    "PU": 'P.U field'
    } 
    ]  

    crypto_from='BTC'
    crypto_to='EUR'
    api_key = "93D86494-DCE3-4077-A9F4-5C36C1D86E34"

    cyptocurrencies = CoinApiIO()
    mesage=cyptocurrencies.GetCryptocurrencies()
    response=requests.get(f'https://rest.coinapi.io/v1/exchangerate/{crypto_from}/{crypto_to}?apikey={api_key}')
    #if status code !=200, sino saco error
    resp_JSON=response.json()
    register = select_all()
    return render_template("index.html", data = JSONstructure,r_JSON=resp_JSON,msg=mesage, reg=register)

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")

@app.route("/status")
def status():
    return render_template("status.html")
