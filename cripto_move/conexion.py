 
import sqlite3
from cripto_move import ORIGIN_DATA

class Conexion:
    def __init__(self,querySql,params = []):#opcional el paso del parametro
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)