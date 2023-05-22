from cripto_move import app
from flask import render_template
from cripto_move.models import *
from cripto_move.database import *

API_key ="93D86494-DCE3-4077-A9F4-5C36C1D86E34"
crypt_dic = [
    {"id" : 0, "name" : "EUR"},
    {"id" : 1, "name" : "BTC"},
    {"id" : 2, "name" : "ETH"}
]

@app.route("/", methods=["GET"])
def index():

    cryptocurrencies = CoinApiIO(crypt_dic)    
    cryptocurrencies.GetCryptocurrencies(API_key)
    
    register = select_all()
    if not register:  
        return render_template("index.html", message="registro vacío")
    else:
        return render_template("index.html", reg=register, )

@app.route("/purchase")
def purchase():
    #consulta de api
    return render_template("purchase.html", crypto_diccion = crypt_dic)#cotizacion actual

@app.route("/status")
def status():
    return render_template("status.html")
