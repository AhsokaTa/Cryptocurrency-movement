from cripto_move import app
from flask import render_template, request
from cripto_move.models import *
from cripto_move.database import *
from config import API_key

@app.route("/", methods=["GET"])
def index():      
        
    #take the ones from database
    my_crypt_register = select_all()

    if not my_crypt_register:  
        return render_template("index.html", message="empty record")
    else:
        return render_template("index.html", reg=my_crypt_register)
    

@app.route("/purchase", methods=["GET","POST"])
def purchase():      

    #all the cryptocurrencies 
    all_crypt = ["EUR","BTC","ETH","USDT", "BNB" , "XRP" , "ADA", "SOL", "DOT", "MATIC"]

    #register, my cryptocurrencies in dictionary format (as it is returned)
    register = select_all() 
    
    #save my cryptocurrencies from the database into the list my_cripto
    my_crypto = []
    for currency in all_crypt:
        for crypto in register:
            if currency == crypto["moneda_to"]:
                my_crypto.append(currency)

###########################################################################################################
                           
    cryptocurrencies = CoinApiIO(all_crypt)   
    my_cryptocurrencies = cryptocurrencies.getCryptocurrencies(API_key) #todas las cripto
    
    respuesta= {}

    if request.method == "GET":
        return render_template ("purchase.html", all_cryp = all_crypt,my_cripto=my_crypto, mis_cripto=my_cryptocurrencies, register=register, rat=0.2, resp_request = respuesta, pre_to="")
    else :
        if request.form['button'] == 'calculate' : 
            q = 000.75666
            pu = float (request.form['from_input_q'])/q

            respuesta = {
                'from_select': request.form['from_select'] ,
                'from_input_q': request.form['from_input_q'],
                'to_select': request.form['to_select'] ,
                'to_labl_q': str(q),
                'to_label_pu':pu                
            }

            all_crypt = ["EUR","BTC","ETH","USDT", "BNB" , "XRP" , "ADA", "SOL", "DOT", "MATIC"]

            return render_template('purchase.html',resp_request = respuesta, all_crypt=all_crypt, pre_to=request.form['to_select'])
        else :
            return "guardar en base de datos sqlite"


@app.route("/status")
def status():
    return render_template("status.html")