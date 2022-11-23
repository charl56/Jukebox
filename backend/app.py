from cmath import e
# import mysql
from sqlFolder.requete_sql import *
#  requeteGetListCd, requeteGetTracklist, requeteCreateAlbum, requeteDeleteThisAlbum, requetePlayThisSong
from flask import Flask, jsonify, request
from flask_cors import CORS
import json 

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})





#Get list cd pour les afficher au debut
@app.route('/listCd', methods=['POST'])
def getListCd():
   try:
      typeRequete = str(request.json['requete'])
      
      listCd = requeteGetListCd(typeRequete)
      print(listCd)

      MyDict_Data = {}
      # MyDict_Data.clear()

      for cd in listCd:
         id = cd[0]
         artiste = cd[1]
         nom_album = cd[2]
         nb_track = cd[3]
         dispo = cd[4]
         album = { 
            'Id':id,
            'Artiste':artiste, 
            'Nom_Album':nom_album, 
            'Nb_Track':nb_track,
            'Dispo':dispo
            }
         print(album)
         MyDict_Data[id]=album
         

      xData_Json = json.dumps(MyDict_Data, indent = 4) 
      print(xData_Json)
      

      xTrackList = requeteGetTracklist()
      xTrackList = json.dumps(xTrackList)
      # ---------------------------
      # Send results back as a json
      resp = {"success": True, "xData": xData_Json, "xTrackList": xTrackList}
      return jsonify(resp), 200 
   
   except Exception as e:
      return "error: " + str(e)

## ----------------------------------------
## Route pour ajouter un cd
@app.route('/SaveSongDb', methods=['POST'])
def SaveSongDb():
   try:
      typeRequete = str(request.json['requete'])
      myAlbum = str(request.json['myAlbum'])
      myArtist = str(request.json['myArtist'])
      mySongNb = str(request.json['mySongNb'])

      print(typeRequete, myAlbum, myArtist, mySongNb)

      requeteCreateAlbum(typeRequete, myAlbum, myArtist, mySongNb)

      ## Save l'image de l'album
      # save_path = '../'
      # file_name = myAlbum+".png"

      # completeName = os.path.join(save_path, file_name)
      # print(completeName)

      # file1 = open(completeName, "w")
      # file1.write("file information")
      # file1.close()

      resp = {"success": True}
      return jsonify(resp), 200 
   except Exception as e:
      return "error: " + str(e)   
## ---------------------------------------------
## Route pour supprimer album
@app.route('/deleteThisAlbum', methods=['POST'])
def deleteThisAlbum():
   try:
      typeRequete = str(request.json['requete'])
      id = request.json['id']

      print(typeRequete, id)

      requeteDeleteThisAlbum(typeRequete, id)

      resp = {"success": True}
      return jsonify(resp), 200 
   except Exception as e:
      return "error: " + str(e)

## ------------------------------------------
## Route pour lancer un son
@app.route('/playThisSong', methods=['POST'])
def playThisSong():
   try:
      print("playThisSong")

      typeRequete = str(request.json['requete'])
      id = request.json['id']
      print(typeRequete, id)

      pos = requetePlayThisSong(typeRequete, id)
      print("pos : ",pos)

      resp = {"success": True, "pos": pos}
      return jsonify(resp), 200 
   except Exception as e:
      return "error: " + str(e)

## ------------------------------------------
## Route pour lancer un son
@app.route('/testImage', methods=['GET'])
def testImage():
   try:
      print("testImage")
      data = "dataaa"
      resp = {"success": True, "xData": data}
      return jsonify(resp), 200 
   except Exception as e:
      return "error: " + str(e)

if __name__ == '__main__':
    # Adresse ip pour créer l'image
    app.run(host='0.0.0.0', port=5025, debug=True)
    # Adresse ip pour lancer en local
    # app.run(host='127.0.0.1', port=5025, debug=True)
