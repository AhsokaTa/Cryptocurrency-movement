import sqlite3
from cripto_move import ORIGIN_DATA
from cripto_move.conexion import Conexion

def select_all():
    dictionary_list = []
    if ("select count(*) FROM tabla") == 0:
        return dictionary_list
    else:
        connect_to=Conexion("select * from movements")

        rows = connect_to.res.fetchall()
        col = connect_to.res.description

        #objetivo crear una lista de diccionario con filas y columnas
        dictionary_list = []

        for f in rows :
            diccionary = {}
            position = 0 
            for c in col : 
                diccionary[c[0]] = f [position]
                position += 1
            dictionary_list.append(diccionary)
        
        connect_to.con.close()

        return dictionary_list