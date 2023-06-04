from cripto_move import app
from flask import render_template, request, flash
from cripto_move.claseCoinApiIp import *
from cripto_move.conexion import *
from cripto_move.modelos import *
from config import API_key, all_crypt
from datetime import datetime


@app.route("/", methods=["GET"])
def index():    
    breadcrumb = "index"
    #take the ones from database
    my_crypt_register = select_all()     

    if not my_crypt_register:  
        return render_template("index.html", message="Sin movimientos, empty record",breadcrumb = breadcrumb)
    else:
        return render_template("index.html", reg=my_crypt_register, breadcrumb=breadcrumb)
    

@app.route("/purchase", methods=["GET","POST"])
def purchase():    

    breadcrumb = "purchase"

    #register, my cryptocurrencies in dictionary format (as it is returned)
    my_crypt_register = select_all_unique()
    
    #save my cryptocurrencies from the database into the list my_cripto
    my_crypto = []
    for currency in all_crypt:
        for crypto in my_crypt_register:
            if currency == crypto["moneda_to"]:
                my_crypto.append(currency)
   
    cryptocurrencies = CoinApiIO(all_crypt)  

    if request.method == "GET":     
        
        return render_template("purchase.html", my_crypto_list = my_crypto, all_crypt_list = all_crypt, quantity_coins = "exchange rate",q_to = "Insert quantity",pre_from = "EUR",pre_to = "Select cryptocurrency",breadcrumb=breadcrumb)

    else :
        if request.form['button'] == 'calculate' : 
            
            value = cryptocurrencies.tradeoCrypto(request.form["quantity"], request.form["from_select"], request.form["to_select"], API_key)                              
            unit_price = float ((value)/float(request.form["quantity"]))
            return render_template('purchase.html',quantity_coins = value, q_to = request.form["quantity"], pre_from = request.form["from_select"], pre_to = request.form["to_select"] , unit_price=unit_price,breadcrumb=breadcrumb)  
        
        else :                
            if request.form["button"] == "save":
                pre_from = request.form["from_select"] 
                pre_q = request.form["quantity"]
                pre_to = request.form["to_select"]
                date_select=datetime.now().date()
                hora_select=datetime.now().strftime("%H:%M:%S")

                add_record([date_select, hora_select, pre_from, pre_q, pre_to, cryptocurrencies.tradeoCrypto(pre_q, pre_from, pre_to , API_key)]) 
                # flash("Movimiento registrado correactamente!!!")        
            return index()


@app.route("/status")
def status():
    
    breadcrumb = "status"
    euros_invested = invested()
    recover = recovered()
    print(type (recover))
    purchase_va = euros_invested-recover
    purchase_va =   f"{purchase_va:.4f}"

    wallet = cartera_de_criptos()

    cryptocurrencies = CoinApiIO(all_crypt)

    crypto_gain=0

    for mon in wallet :
        valor_moneda = cryptocurrencies.crytocurrenciesValue(mon['moneda'], API_key)
        crypto_gain += mon['total_cripto'] * valor_moneda    
       
    return render_template("status.html", invested = euros_invested, recover=recover,purchase_va=purchase_va, 
                           breadcrumb=breadcrumb, crypto_gain=crypto_gain)