from cripto_move import app

@app.route("/")
def inde():
    return "Flask Skeleton"