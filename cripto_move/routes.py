from cripto_move import app
from flask import render_template
from cripto_move.models import *
from cripto_move.database import *
from config import API_key

crypt_dic = [
    {"id" : 0, "name" : "EUR"},
    {"id" : 1, "name" : "BTC"},
    {"id" : 2, "name" : "ETH"},
    {"id" : 3, "name" : "ADA"}
]
all_crypt = [
    {"id" : 0, "name" : "EUR"},
    {"id" : 1, "name" : "BTC"},
    {"id" : 2, "name" : "ETH"},
    {"id" : 3, "name" : "USDT"},
    {"id" : 4, "name" : "BNB"},
    {"id" : 5, "name" : "XRP"},
    {"id" : 6, "name" : "ADA"},
    {"id" : 7, "name" : "SOL"},
    {"id" : 8, "name" : "DOT"},
    {"id" : 9, "name" : "MATIC"}
]

my_crypt=[]
my_crypt=select_all()

#crear diccionario con las cripto totales
#crear un diccionario con las cripto que tnego en base de datos 
@app.route("/", methods=["GET"])
def index():

    cryptocurrencies = CoinApiIO(crypt_dic)    
    cryptocurrencies.getCryptocurrencies(API_key)
    
    register = select_all()
    if not register:  
        return render_template("index.html", message="empty record")
    else:
        return render_template("index.html", reg=register)
    #return jsonify()

@app.route("/purchase", methods=["GET", "POST"])
def purchase():       
    #consulta de api    
    
    cryptocurrencies = CoinApiIO(crypt_dic)    
    rate = cryptocurrencies.crytocurrenciesValue("BTC",API_key)
    
    register = select_all()
    if not register:
        return render_template("purchase.html", all_cryp = all_crypt)
    else :       
        return render_template("purchase.html", all_cryp = all_crypt, reg=register,rat=rate)

@app.route("/status")
def status():
    return render_template("status.html")
