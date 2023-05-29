 
import sqlite3
from cripto_move import ORIGIN_DATA

class Conexion:
                                #parameter is optional
    def __init__(self,querySql , params = []):
        self.con = sqlite3.connect(ORIGIN_DATA)
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySql,params)    

    def select_all():

        dictionary_list = []
        if ("select count(*) FROM tabla") == 0:
            return dictionary_list
        else:
            #future improvement: sort by a specific field
            connect_to=Conexion("select * from movements") 

            rows = connect_to.res.fetchall()
            col = connect_to.res.description

            #create a list of dictionaries with rows and columns
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
        
    def select_all_unique():

        dictionary_list = []
        if ("select count(*) FROM tabla") == 0:
            return dictionary_list
        else:           
            connect_to=Conexion("SELECT DISTINCT moneda_from, moneda_to FROM movements") 

            rows = connect_to.res.fetchall()
            col = connect_to.res.description

            #create a list of dictionaries with rows and columns
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
    
    def add_record():
        pass

    def add_record(registroForm):
        conectarNuevo = Conexion("INSERT INTO movements(date,time,moneda_from, cantidad_from, moneda_to,cantidad_to) VALUES(?,?,?,?,?,?)", registroForm)
        conectarNuevo.con.commit()
        conectarNuevo.con.close()





        


        