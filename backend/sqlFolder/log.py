#import pyodbc
#import mysql.connector
import mariadb

def loginToDB(database, username, password):
    try:
        print(database, username, password)
        #conn = mysql.connector.connect(
        conn = mariadb.connect(

            host="localhost",
            database=database, 
            user=username,
            passwd=password)
        print(conn)
        print("aaa")
        return conn

    except ValueError:
        print("Connexion issue : "+ ValueError)
