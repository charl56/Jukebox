<template>
  <div id="idTable" class="tableAlbum">

    <div id="albums">
      <div class="boxAlbum"
            v-for="item in cd_list" 
            :key="item.id" 
            v-bind:id="item.Id" 
            :class="{ dispo: item.Dispo==1, nonDispo: item.Dispo==0}"
            @click=openThis(item)>

          <v-img id="pochette" :src="getImageUrl(item.Nom_Album)"> </v-img>
          <p >{{item.Nom_Album}}</p>


      </div>


    </div>

    <v-dialog v-model="dialog" transition="dialog-top-transition" height="100vh" width="50vw">
          <v-card>
              <v-card-title>
                <v-col cols="12" sm="12" md="12" >
                  <span class="text-h4">{{myAlbumModal}}</span>
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
                              <!-- <img class="classImageAlbum" :src="getImageUrl(myAlbumModal)"> -->
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
                <v-col cols="12" sm="4" md="4">
                  <v-btn color="red darken-1" text @click="deleteThisAlbum" >
                      Supprimer
                  </v-btn>
                </v-col>
                <v-col cols="12" sm="4" md="4">
                  <v-btn color="blue darken-1" text @click="editThisAlbum" >
                      Modifier
                  </v-btn>
                </v-col>
                <v-col cols="12" sm="4" md="4">
                  <v-btn color="green darken-1" text @click="editThisAlbum" >
                      <v-img @click="playThisSong" src="../../assets/logo/logo.png" class="image" ></v-img>
                  </v-btn>
                </v-col>


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
      track: '',
      cd_list: null
    }
  },
  methods:{
    /* Reçoit requete du component , post requete axios au back, puis envoie les données au component TrendLine */
    async listCd() {
      // this.$root.$refs.Header.loadingBar("visible");
      console.log("fonction requete requeteGetListCd")
      const postData = { requete: "getListCd"};
      await axios.post(this.$flaskUrl+"/listCd", postData)
        .then(response => {
          console.log(response.status);
          // Liste de cd
          var Json_xData = JSON.parse(response.data.xData)
          this.cd_list = null
          this.cd_list = Json_xData
          console.log("liste en Json", Json_xData)
          console.log(JSON.parse(response.data.xTrackList))
          
        }).catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
      // this.$root.$refs.Header.loadingBar("visible");
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
    openThis(item){
      console.log("item : ", item)
      this.dialog = true;
      this.myArtistModal = item.Artiste;
      this.myAlbumModal = item.Nom_Album;
      this.myIdModal = item.Id;
      this.mySongNbModal = item.Nb_Track;
    },
    getImageUrl(album){
      console.log(album)
      var image = require("../../assets/photosAlbums/"+album.split(' ').join('_')+".jpg")
      return image
    }
  },
  computed: {


  }
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

.tableAlbum{
  margin-top: 1em;
  height: 20em;
  width: 100%;
  display: flex;
  justify-content: center;
}

.boxAlbum{
  border-radius: 1em;
  width: 175px;
  height: 175px;
  margin: 1em 2em;
  float: left;
  opacity: 0.85;
}.boxAlbum > p{
  font-size: 0px;
}.boxAlbum:hover > p{
  font-size: 3vh;
}
#pochette{
  border-radius: 1em;
}
.dispo{
  background-color: #FFC9A3;
}.dispo.boxAlbum:hover{
  cursor: pointer;
}
.nonDispo{
  background-color: #B1BAC7;
  opacity: 0.6;
}.nonDispo.boxAlbum:hover{
  cursor: pointer ;
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

