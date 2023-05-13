from cripto_move import app
from flask import render_template


@app.route("/")
def inde():
    #return "Flask Skeleton"
    return render_template("index.html")