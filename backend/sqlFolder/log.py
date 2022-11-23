# import pyodbc
import mysql.connector


def loginToDB(database, username, password):
    try:
        ## Pour le build en docker ##FreeTDS
        # conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
        #     'SERVER='+'0.0.0.0'+';'
        #     'DATABASE='+database+';'
        #     'UID='+username+';'
        #     'PWD='+ password)

        conn = mysql.connector.connect(
            host="localhost",
            database=database, 
            user=username,
            password=password)
        return conn

    except ValueError:
        print("Connexion issue : "+ ValueError)