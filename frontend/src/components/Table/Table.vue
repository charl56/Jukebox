<template>
  <div id="idTable" class="tableAlbum">

    <div id="albums">
      <!-- <img class="classImageAlbum" src="../../assets/photosAlbums/La vie de luxe.jpg"> -->
    </div>

    <v-dialog v-model="dialog" transition="dialog-bottom-transition" max-width="600px">
          <v-card>
              <v-card-title>
                <v-col cols="12" sm="9" md="3" >
                  <span class="text-h4">{{myAlbumModal}}</span>
                </v-col>
                <v-col cols="12" sm="3" md="3" >
                  <v-img @click="playThisSong" src="../../assets/logo/logo.png" class="image" ></v-img>
                </v-col>
              </v-card-title>
              <v-card-text>
                  <v-container id="v-container-album">
                      <v-row>
                          <v-col cols="12" sm="8" md="8" >
                            <v-row>
                              <span class="text-h5">Artiste : {{myArtistModal}}</span>
                            </v-row>
                            <v-row id="rowImageAlbum">
                              <img class="classImageAlbum" :src="'../../assets/photosAlbums/'+myAlbumModal+'.jpg'">
                            </v-row>
                          </v-col>
                          <v-col cols="12" sm="4" md="4">
                            Liste des titres
                            <div id="tracklist">
                            </div>
                          </v-col>
                      </v-row>
                  </v-container>
              </v-card-text>
              <v-card-actions>
                  <v-btn color="blue darken-1" text @click="deleteThisAlbum" >
                      Supprimer
                  </v-btn>
                  <v-btn color="blue darken-1" text @click="editThisAlbum" >
                      Modifier
                  </v-btn>
              </v-card-actions>
          </v-card>
      </v-dialog>
  </div>

</template>

<script  >
import axios from 'axios';


export default {
  name: 'AppTable',
  created(){
    this.$root.$refs.Table = this;
  }
  ,
  mounted(){ // Lance la fonction au chargement de la page
    axios
      .get('https://data.angers.fr/api/v2/catalog/datasets/irigo_gtfs_lines/exports/json')
      .then(reponse =>{
        console.log(reponse.data)
      }).catch(error => {
      this.errorMessage = error.message;
      console.error("There was an error with data angers", error);
    });
    axios
    .get("http://localhost:5025/testImage")
      .then(response => {
        console.log(response.data);
      }).catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error with localhost", error);
    });
    this.listCd();
  },
  data () {
    return {
      dialog: false,
      myAlbum: '',
      myArtist: '',
      mySongNb:'',      
      myAlbumModal: '',
      myArtistModal: '',
      mySongNbModal:'',
      myIdModal: '',
      track: ''
    }
  },
  methods:{
    /* Reçoit requete du component , post requete axios au back, puis envoie les données au component TrendLine */
    async listCd() {
      this.$root.$refs.Header.loadingBar("visible");
      console.log("fonction requete requeteGetListCd")
      const postData = { requete: "getListCd"};
      await axios.post(this.$flaskUrl+"/listCd", postData)
        .then(response => {
          console.log(response.status);
          var Json_xData = JSON.parse(response.data.xData)
          var xTrackList = JSON.parse(response.data.xTrackList)
          console.log("liste en Json", Json_xData)
          console.log("TrackList", xTrackList)
          
          // Permet de ne pas avoir de double au recharchement de la page
          const elements = document.getElementsByClassName('boxAlbum');
          while(elements.length > 0){
              elements[0].parentNode.removeChild(elements[0]);
          }

          // Créer les div pour chaque album
          for (const albumDb in Json_xData){           
            const el = document.createElement('div');
            el.classList.add('boxAlbum');
            el.setAttribute('id', 'photoAlbumBox');

            if(Json_xData[albumDb].Dispo == 1){
              el.classList.add('dispo');
            }else{
              el.classList.add('nonDispo');
            }
            // Mettre en variable les données recus
            this.myArtist = Json_xData[albumDb].Artiste
            this.myAlbum = Json_xData[albumDb].Nom_Album
            this.mySongNb = Json_xData[albumDb].Nb_Track
            // Ajout de la photo au background
            // const img = document.createElement('img');
            // img.src = "../../assets/photosAlbums/La_vie_de_luxe.jpg"
            // document.getElementById("photoAlbumBox").appendChild(img);


            // el.style.backgroundImage = "url('./assets/photosAlbums/La_vie_de_luxe.jpg')";
            el.addEventListener('click', () => {
              // Ouvrir le modale
              this.dialog = true;
              console.log(Json_xData[albumDb].Artiste, Json_xData[albumDb].Nom_Album);
              // Variables modale
              this.myArtistModal = Json_xData[albumDb].Artiste;
              this.myAlbumModal = Json_xData[albumDb].Nom_Album;
              this.myIdModal = Json_xData[albumDb].Id;
              this.mySongNbModal = Json_xData[albumDb].Nb_Track;
            });
            el.innerHTML = "<h4>"+this.myArtist+"</h4><h5>"+this.myAlbum+"<br>Nombre de sons : "+this.mySongNb+"</h5>";
            document.getElementById('albums').appendChild(el);        
          }

           // Créer les div pour chaque track de l'album
          for (const tracks in xTrackList){           
            const el = document.createElement('div');
            el.classList.add('boxTrack');
            this.track = tracks
            el.addEventListener('click', (event) => {
              console.log(event);
              console.log(this.track);
            });
            el.innerHTML = "<h4>"+this.myAtrackrtist+"</h4>";
            // const box = document.getElementById('tracklist');
            // box.appendChild(el);        
          }
        }).catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
      this.$root.$refs.Header.loadingBar("visible");
    },
    async deleteThisAlbum(){
      if (confirm("Voulez-vous supprimer l'album de "+ this.myArtistModal)) {
        console.log("ok")
        const postData = { requete: "deleteThisAlbum", id: this.myIdModal};
        await axios.post(this.$flaskUrl+"/deleteThisAlbum", postData)
        .then(response => {
          console.log(response.status);              
        }).catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
        this.listCd();
        this.dialog = false;
      } else {
        console.log("nop")
      }
    },
    editThisAlbum(){
  
    },
    async playThisSong(){
      console.log("play : ",this.myAlbumModal);
      const postData = { requete: "playThisSong", id: this.myIdModal};
      await axios.post(this.$flaskUrl+"/playThisSong", postData)
      .then(response => {
        console.log(response.status);              
        console.log("positions : "+response.data.pos);              
      }).catch(error => {
        this.errorMessage = error.message;
        console.error("There was an error!", error);
      });
    },
    getImageAlbum(){
      return this.myAlbumModal
    }
  },
  computed: {
    setImageAlbum(){      
      return `${require(`@/assets/photosAlbums/${this.myAlbumModal}.jpg`)}`

    }


  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

.tableAlbum{
  /* background-color: #d2cccc; */
  height: 20em;
  width: 100%;
  display: flex;
  justify-content: center;
}

.boxAlbum{
  border-radius: 1em;
  width: 150px;
  height: 150px;
  margin: 1em 2em;
  float: left;
}
.dispo{
  background-color: antiquewhite;
}
.boxAlbum:hover{
  cursor: pointer;
  background-color: rgb(255, 213, 155);
  /* margin-left: 20px solid red;
  border-right: 20px solid green; */
}
.nonDispo{
  background-color: rgb(124, 124, 124);
}

.image{
  height: 3em;
  width: 3em;
  cursor: pointer;
}
.classImageAlbum{
  height: 5em !important;
  width: 5em !important;
}

</style>

