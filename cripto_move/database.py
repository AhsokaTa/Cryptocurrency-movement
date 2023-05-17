import sqlite3
from cripto_move import ORIGIN_DATA

def select_all():
    con = sqlite3.connect(ORIGIN_DATA)
    cur = con.cursor()
    res = cur.execute("select * from movements")
    rows = res.fetchall()
    col = res.description

    #objetivo crear una lista de diccionario con filas y columnas
    dictionary_list = []

    for f in rows :
        diccionary = {}
        position = 0 
        for c in col : 
            diccionary[c[0]] = f [position]
            position += 1
        dictionary_list.append(diccionary)
    
    con.close()

    return dictionary_list