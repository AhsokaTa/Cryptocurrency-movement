from flask import Flask

app = Flask (__name__)

ORIGIN_DATA = "data/movements.sqlite"

from cripto_move.routes import *