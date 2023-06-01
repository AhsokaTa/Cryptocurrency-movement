from cripto_move import app
from flask import render_template, request, flash
from cripto_move.models import *
from cripto_move.conexion import *
from config import API_key

from datetime import datetime

"""
desactivar /index, /purchase, /status 

si le da al boton calcular o al boton saver, consultar a BASE DATOS la suma de monedas 
con las que quiere comprar

"""

@app.route("/", methods=["GET"])
def index():    
    
    #take the ones from database
    my_crypt_register =Conexion.select_all()     

    if not my_crypt_register:  
        return render_template("index.html", message="Sin movimientos, empty record")
    else:
        return render_template("index.html", reg=my_crypt_register)
    

@app.route("/purchase", methods=["GET","POST"])
def purchase():      

    #all the cryptocurrencies 
    all_crypt = ["EUR","BTC","ETH","USDT", "BNB" , "XRP" , "ADA", "SOL", "DOT", "MATIC"]

    #register, my cryptocurrencies in dictionary format (as it is returned)
    my_crypt_register = Conexion.select_all_unique()
    
    #save my cryptocurrencies from the database into the list my_cripto
    my_crypto = []
    for currency in all_crypt:
        for crypto in my_crypt_register:
            if currency == crypto["moneda_to"]:
                my_crypto.append(currency)
   
    cryptocurrencies = CoinApiIO(all_crypt)  

    if request.method == "GET":     
        
        return render_template("purchase.html", my_crypto_list = my_crypto, all_crypt_list = all_crypt, quantity_coins = "exchange rate",q_to = "Insert quantity",pre_from = "EUR",pre_to = "Select cryptocurrency")

    else :
        if request.form['button'] == 'calculate' : 
            
            value = cryptocurrencies.tradeoCrypto(request.form["quantity"], request.form["from_select"], request.form["to_select"], API_key)                              
            unit_price=float ((value)/float(request.form["quantity"]))
            return render_template('purchase.html',quantity_coins = value, q_to = request.form["quantity"], pre_from = request.form["from_select"], pre_to = request.form["to_select"] , unit_price=unit_price)  
        
        else :                
            if request.form["button"] == "save":
                pre_from = request.form["from_select"] 
                pre_q = request.form["quantity"]
                pre_to = request.form["to_select"]
                date_select=datetime.now().date()
                hora_select=datetime.now().strftime("%H:%M:%S")
                """ modificacion 16:40
                if request.form["to_select"] == "EUR":
                    valor = cryptocurrencies.crytocurrenciesValue(pre_from, API_key)  
                    
                else:
                    valor = cryptocurrencies.crytocurrenciesValue(pre_to, API_key)
                """

                Conexion.add_record([date_select, hora_select, pre_from, pre_q, pre_to, cryptocurrencies.tradeoCrypto(pre_q, pre_from, pre_to , API_key)]) 
               # flash("Movimiento registrado correactamente!!!")        
            return index()


@app.route("/status")
def status():
    
    euros_invested = Conexion.invested()
    recover = Conexion.recovered()

    #int_reco=recover
    #recover_str= f"{recover:.7f}"
    #recover = f"{recover:.4f}"
    print(type (recover))
    purchase_va=euros_invested-recover
    purchase_va =   f"{purchase_va:.4f}"
    
    return render_template("status.html", invested = euros_invested, recover=recover,purchase_va=purchase_va)