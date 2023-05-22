from cripto_move import app
from flask import render_template
from cripto_move.models import *
from cripto_move.database import *

API_key ="93D86494-DCE3-4077-A9F4-5C36C1D86E34"

@app.route("/", methods=["GET"])
def index():
    
    cryptocurrencies = CoinApiIO()    
    cryptocurrencies.GetCryptocurrencies(API_key)
    
    register = select_all()
    return render_template("index.html", reg=register)

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")

@app.route("/status")
def status():
    return render_template("status.html")
