from cripto_move import app
from flask import render_template, request
from cripto_move.models import *
from cripto_move.database import *
from config import API_key

crypt_dic = [
    {"id" : 0, "name" : "EUR"},
    {"id" : 1, "name" : "BTC"},
    {"id" : 2, "name" : "ETH"},
    {"id" : 3, "name" : "ADA"}
]

all_crypt = ["EUR","BTC","ETH","USDT", "BNB" , "XRP" , "ADA", "SOL", "DOT", "MATIC"]

my_crypt=[]
my_crypt=select_all()

#crear diccionario con las cripto totales
#crear un diccionario con las cripto que tnego en base de datos 

@app.route("/", methods=["GET"])
def index():

    cryptocurrencies = CoinApiIO(all_crypt)    
    #cryptocurrencies.getCryptocurrencies(API_key)
    
    register = select_all()
    if not register:  
        return render_template("index.html", message="empty record")
    else:
        return render_template("index.html", reg=register)
    #return jsonify()

@app.route("/purchase", methods=["GET","POST"])
def purchase():       
    #consulta de api    

    all_crypt = ["EUR","BTC","ETH","USDT", "BNB" , "XRP" , "ADA", "SOL", "DOT", "MATIC"]
    
    cryptocurrencies = CoinApiIO(crypt_dic)    

    """
    register = select_all()
    if not register:
        return render_template("purchase.html", all_cryp = all_crypt)
    else :       
        return render_template("purchase.html", all_cryp = all_crypt, reg=register,rat=rate)
    """ 

    #rate = cryptocurrencies.crytocurrenciesValue("BTC" , API_key)
    
    register = select_all()  
    respuesta= {}

    if request.method == "GET":
        return render_template ("purchase.html", all_cryp = all_crypt, reg=register, rat=0.2, resp_request = respuesta, pre_to="")
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