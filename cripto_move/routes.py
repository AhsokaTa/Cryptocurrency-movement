from cripto_move import app
from flask import render_template


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
    return render_template("index.html", data = JSONstructure)

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")

@app.route("/status")
def status():
    return render_template("status.html")
