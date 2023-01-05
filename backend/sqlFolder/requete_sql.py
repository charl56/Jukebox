from sqlFolder.class_requetes import getSqlQueryString
# import numpy as np
import sqlite3
from sqlFolder.log import loginToDB 
from dotenv import dotenv_values

## Requetes qui va chercher la requete sql, par jours
# def requete(fileName, startDate, endDate, frequence):
def requeteGetListCd(typeRequete):
    try :        
        # Connexion BDD
        config = dotenv_values("env/log.env")
        # server = config.get("server")
        # database = config.get("database")
        username = config.get("username")
        password = config.get("password")

        conn = loginToDB("jukebox", username, password)
        cursor = conn.cursor()

        requete_sql = getSqlQueryString("sqlFolder/query/"+typeRequete+".sql")
        # requete_sql = getSqlQueryString("sqlFolder/query/get"+fileName+"Par"+frequence+".sql")

        ##Execute dans la BDD la requete sql, recupere le cursor de connection
        cursor.execute(requete_sql)
        # cursor.execute(requete_sql,startDate,endDate)
        print("exectute commande sql")


        data = cursor.fetchall() ## transformer vers un tableau 2D (par contre on a plus les en-têtes)
        print("Sortie bdd")

        conn.close()

        return data

    except sqlite3.Error as error:
        print("Failed to read data from table", error)

def requeteGetTracklist():
    try :        
        # Connexion BDD
        config = dotenv_values("env/log.env")
        # server = config.get("server")
        # database = config.get("database")
        username = config.get("username")
        password = config.get("password")

        conn = loginToDB("jukebox", username, password)
        cursor = conn.cursor()

        requete_sql = getSqlQueryString("sqlFolder/query/getTracklist.sql")

        ##Execute dans la BDD la requete sql, recupere le cursor de connection
        cursor.execute(requete_sql)
        # cursor.execute(requete_sql,startDate,endDate)
        print("exectute commande sql")


        data = cursor.fetchall() ## transformer vers un tableau 2D (par contre on a plus les en-têtes)
        print("Sortie bdd")

        conn.close()

        return data

    except sqlite3.Error as error:
        print("Failed to read data from table", error)


def requeteCreateAlbum(typeRequete, myAlbum, myArtist, mySongNb):
    try :        
        # Connexion BDD
        config = dotenv_values("env/log.env")
        # server = config.get("server")
        # database = config.get("database")
        username = config.get("username")
        password = config.get("password")

        conn = loginToDB("jukebox", username, password)
        cursor = conn.cursor()
        print("connecte bdd")

        requete_sql = getSqlQueryString("sqlFolder/query/"+typeRequete+".sql")

        ##Execute dans la BDD la requete sql, recupere le cursor de connection
        album = (myArtist, myAlbum, int(mySongNb), 0, 0, 1)
        cursor.execute(requete_sql, album)
        conn.commit()    

        print(cursor.rowcount, "record inserted.")

        # cursor.execute(requete_sql,startDate,endDate)
        print("exectute commande sql")

        conn.close()


    except sqlite3.Error as error:
        print("Failed to read data from table", error)



def requeteDeleteThisAlbum(typeRequete, id):
    try :        
        # Connexion BDD
        config = dotenv_values("env/log.env")
        # server = config.get("server")
        # database = config.get("database")
        username = config.get("username")
        password = config.get("password")

        conn = loginToDB("jukebox", username, password)
        cursor = conn.cursor()
        print("connecte bdd")

        requete_sql = getSqlQueryString("sqlFolder/query/"+typeRequete+".sql")

        ##Execute dans la BDD la requete sql, recupere le cursor de connection
    
        cursor.execute(requete_sql, [id])
        conn.commit()    

        # cursor.execute(requete_sql,startDate,endDate)
        print("exectute commande sql")

        conn.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)



def requetePlayThisSong(typeRequete, id):
    print("requetePlayThisSong", typeRequete, id)

    try :        
        # Connexion BDD
        config = dotenv_values("env/log.env")
        # server = config.get("server")
        # database = config.get("database")
        username = config.get("username")
        password = config.get("password")

        conn = loginToDB("jukebox", username, password)
        cursor = conn.cursor()
        print("connecte bdd")

        requete_sql = getSqlQueryString("sqlFolder/query/"+typeRequete+".sql")

        ##Execute dans la BDD la requete sql, recupere le cursor de connection
    
        cursor.execute(requete_sql, [id])
        data = cursor.fetchall()
        print(data)

        conn.commit()    

        # cursor.execute(requete_sql,startDate,endDate)
        print("exectute commande sql")

        conn.close()

        return data

    except sqlite3.Error as error:
        print("Failed to read data from table", error)



def requeteEditCdPosition(typeRequete, id, cdPositionX, cdPositionY):
    try :        
        # Connexion BDD
        config = dotenv_values("env/log.env")
        # server = config.get("server")
        # database = config.get("database")
        username = config.get("username")
        password = config.get("password")

        conn = loginToDB("jukebox", username, password)
        cursor = conn.cursor()
        print("connecte bdd")

        requete_sql = getSqlQueryString("sqlFolder/query/"+typeRequete+".sql")

        ##Execute dans la BDD la requete sql, recupere le cursor de connection
        edit = (cdPositionX, cdPositionY, id)
        cursor.execute(requete_sql, edit)
        conn.commit()    

        # cursor.execute(requete_sql,startDate,endDate)
        print("exectute commande sql")

        conn.close()


    except sqlite3.Error as error:
        print("Failed to read data from table", error)





















# def playThisSong(typeRequete, id):
#     try :        
#         # Connexion BDD
#         config = dotenv_values("env/log.env")
#         # server = config.get("server")
#         # database = config.get("database")
#         username = config.get("username")
#         password = config.get("password")

#         conn = loginToDB("jukebox", username, password)
#         cursor = conn.cursor()
#         print("connecte bdd")

#         requete_sql = getSqlQueryString("sqlFolder/query/"+typeRequete+".sql")

#         ##Execute dans la BDD la requete sql, recupere le cursor de connection
    
#         cursor.execute(requete_sql, [id])
#         conn.commit()    
#         # print(cursor.fetchall()) ## transformer vers un tableau 2D (par contre on a plus les en-têtes)
#         # cursor.execute(requete_sql,startDate,endDate)
#         print("exectute commande sql")

#         conn.close()

#         # return "OK"

#     except sqlite3.Error as error:
#         print("Failed to read data from table", error)