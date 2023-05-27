from cripto_move import app
from flask import render_template, request
from cripto_move.models import *
from cripto_move.conexion import *

from config import API_key

@app.route("/", methods=["GET"])
def index():    
        
    #take the ones from database
    my_crypt_register =Conexion.select_all()     

    if not my_crypt_register:  
        return render_template("index.html", message="empty record")
    else:
        return render_template("index.html", reg=my_crypt_register)
    

@app.route("/purchase", methods=["GET","POST"])
def purchase():      

    #all the cryptocurrencies 
    all_crypt = ["EUR","BTC","ETH","USDT", "BNB" , "XRP" , "ADA", "SOL", "DOT", "MATIC"]

    #register, my cryptocurrencies in dictionary format (as it is returned)
    my_crypt_register = Conexion.select_all() 
    
    #save my cryptocurrencies from the database into the list my_cripto
    my_crypto = []
    for currency in all_crypt:
        for crypto in my_crypt_register:
            if currency == crypto["moneda_to"]:
                my_crypto.append(currency)

###########################################################################################################
                         
    cryptocurrencies = CoinApiIO(all_crypt)   
    my_cryptocurrencies = cryptocurrencies.getCryptocurrencies(API_key) #todas las cripto
    
    
    respuesta= {}

    if request.method == "GET":     
        
        return render_template("purchase.html", my_crypto_list = my_crypto, all_crypt_list = all_crypt, quantity_coins = "exchange rate",q_to = "Insert quantity",pre_from = "EUR",pre_to = "Select cryptocurrency")

    else :
        if request.form['button'] == 'calculate' : 

            """
            q = 000.75666
            pu = float (request.form['from_input_q'])/q
            """
            
            respuesta = { 
                            "pre_from" : request.form["from_select"], 
                            "pre_q" : request.form["quantity"],
                            "pre_to" : request.form["to_select"]
                        }
            value = cryptocurrencies.tradeoCrypto(request.form["quantity"], request.form["from_select"], request.form["to_select"], API_key)
                                   
            return render_template('purchase.html',quantity_coins = value, q_to = request.form["quantity"], pre_from = request.form["from_select"], pre_to = request.form["to_select"] )  
        
        else :
            
            return "guardar en base de datos sqlite"


@app.route("/status")
def status():
    return render_template("status.html")