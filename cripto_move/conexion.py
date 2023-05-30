 
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
    

    def add_record(registroForm):
        conectarNuevo = Conexion("INSERT INTO movements(date,time,moneda_from, cantidad_from, moneda_to,cantidad_to) VALUES(?,?,?,?,?,?)", registroForm)
        conectarNuevo.con.commit()
        conectarNuevo.con.close()

    
    def invested():
        connect_to = Conexion("SELECT SUM(Cantidad_from) AS total_cantidad_from FROM movements WHERE moneda_from = 'EUR'")
        row = connect_to.res.fetchone()  # Obtener la primera fila de resultados

        connect_to.con.close()

        if row and row[0] is not None:
            return int(row[0])
        else:
            return 0

    def recovered():
        connect_to = Conexion("SELECT SUM(cantidad_to) AS total_euros_obtenidos FROM movements WHERE moneda_to = 'EUR'")
        row = connect_to.res.fetchone()  # Obtener la primera fila de resultados

        connect_to.con.close()

        if row and row[0] is not None:
            total_euros = row[0]            
            return total_euros #total de euros
        else:            
            return 0 #no hay nada


    def current_value_euros():
        pass

    """
    def invested():
        
        Invertido: Es el total de euros con el que se han comprado criptos. Se calcula como 
        la suma de la columna Cantidad_from de todos los movimientos cuya Moneda_from es EUROS.
        
        connect_to = Conexion("SELECT SUM(Cantidad_from) AS total_cantidad_from FROM movements WHERE moneda_from = 'EUR'") 

        rows = connect_to.res.fetchall()
        col = connect_to.res.description

        dictionary_list = []

        for row in rows:
            dictionary = dict(zip([column[0] for column in col], row))
            dictionary_list.append(dictionary)

        connect_to.con.close()

        return dictionary_list if dictionary_list else []
    _____________________________

    def invested():

        dictionary_list = []
        
        connect_to=Conexion("SELECT SUM(Cantidad_from) AS total_cantidad_from FROM movements WHERE moneda_from = 'EUR'") 

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


_____________________


    def recovered():
        
        Recuperado: Es el total de euros obtenidos con la venta de cualquier cripto (registrada en nuestro sistema). Se calcula como 
        la suma de la columna Cantidad_to de todos los movimientos cuya Moneda_to es EUROS.
        
        connect_to = Conexion("SELECT SUM(cantidad_to) AS total_euros_obtenidos FROM movements WHERE moneda_to = 'EUR'") 

        rows = connect_to.res.fetchall()
        col = connect_to.res.description

        dictionary_list = []

        for row in rows:
            dictionary = dict(zip([column[0] for column in col], row))
            dictionary_list.append(dictionary)

        connect_to.con.close()

        return dictionary_list if dictionary_list else []
        """