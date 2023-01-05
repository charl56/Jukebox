<template>
  <div id="idTable" class="tableAlbum">


    <!-- <div v-if="n == 3 && k == 2" class="background2">
          f
        </div>
        <div v-else md="2" class="background" >
          aaaa {{n}}, {{k}}
        </div> -->
<!--
      <div class="" v-for="n in 5" :key="n" >
        <v-col class="" v-for="k in 3" :key="k" cols="10" sm="2">
          <div class="background" >
            aaaa {{n}}, {{k}}
          </div>
        </v-col>
      </div> -->

      <!-- <v-content class="px-5">
        <v-data-iterator
          :items="cd_list"
          item-key="Id"
          :items-per-page="5"
        >
        <template>
          <v-row class="fill-height overflow-auto" id="container">
            <v-col
              v-for="item in cd_list"
              :key="item.Id"
              :cols="(4)"
              class="py-2"
            >
              <v-card class="card fill-height">
                <v-card-title>
                    <span class="font-weight-light text-truncate">
                      <span v-text="item.Id"></span> {{ item.Nom_Album }}
                    </span>
                </v-card-title>
              </v-card>
            </v-col>
          </v-row>
        </template>

      </v-data-iterator>
    </v-content>
 -->


    <v-col class="height-100 d-flex justify-center align-center" cols="12" sm="8" md="9">
      <div id="albums">
        <div class="boxAlbum"
          v-for="item in cd_list"
          :key="item.id"
          v-bind:id="item.Id"
          :class="{ dispo: item.Dispo==1, nonDispo: item.Dispo==0}"
          @click=openThis(item)
          >
           <v-img id="pochette" :src="getImageUrl(item.Nom_Album)"> </v-img>
          <p >{{item.Nom_Album}}</p>
        </div>
      </div>
    </v-col>
    <v-col class="height-100 d-flex justify-center align-center" cols="12" sm="4" md="3">
      <div class="div-cd">
          <v-img :src="getImageUrl(url)" class="image-cd d-flex align-center" id="cd-play">
            <div class="" id="centre-cd"></div>
          </v-img>
          <!-- <button  >Stop</button> -->
          <div class="d-flex align-center justify-center">
            <v-img class="btn-music" @click="replayThisSong()" src="../../assets/logoButtons/play-circle-outline.png"> </v-img>
            <v-img class="btn-music" @click="pauseThisSong()" src="../../assets/logoButtons/pause-circle-outline.png"> </v-img>
            <v-img class="btn-music" @click="stopThisSong()" src="../../assets/logoButtons/stop-circle-outline.png"> </v-img>
          </div>

      </div>
    </v-col>







    <v-dialog v-model="dialog" transition="dialog-top-transition" height="100vh" width="50vw" persistent>
          <v-card>
              <v-card-title>
                <v-col cols="12" offset="3" sm="6" md="6" >
                  <span class="text-h4">{{myAlbumModal}}</span>
                </v-col>
                <v-col cols="12" sm="3" md="3" >
                  <button @click="toggleDialog()">X</button>
                </v-col>
              </v-card-title>
              <v-card-text>
                  <v-container id="v-container-album">
                      <v-row>
                          <v-col cols="12" sm="8" md="8" >
                            <v-row class="block">
                              <h1 class="text-h5">Artiste : {{myArtistModal}}</h1>
                              <button @click="toggleEditCdPosition" class="text-h6">Modifier la position du cd</button>
                              <v-card v-if="showModalEditCdPosition" id="ModalCdPosition">
                                <div>
                                  <form @submit="saveCdPosition" method="post">
                                    <input class="input-add" type="number" :placeholder="myAlbumPosX"  v-model="myAlbumPosX2">
                                    <input class="input-add" type="number" :placeholder="myAlbumPosY"  v-model="myAlbumPosY2">
                                    <div>
                                      <input class="" id="cancel-register"  type="button" value="Annuler" v-on:click="toggleEditCdPosition()">
                                      <input class="" type="submit" value="Enregistrer" >
                                    </div>
                                  </form>

                                </div>
                              </v-card>

                            </v-row>
                            <v-row id="rowImageAlbum">
                              <!-- <img class="classImageAlbum" :src="getImageUrl()"> -->
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
                  <v-btn color="green darken-1" text>
                      <v-img @click="playThisSong" src="../../assets/logo/logo.png" class="imagePlay" ></v-img>
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
      myAlbumPosX: '',
      myAlbumPosX2: null,
      myAlbumPosY: '',
      myAlbumPosY2: null,
      track: '',
      cd_list: null,
      showModalEditCdPosition: false,
      url: 'no_disque',
    }
  },
  methods:{
    toggleDialog(){
      this.dialog = !this.dialog
      this.myAlbumPosX2 = this.myAlbumPosY2 = null
      this.showModalEditCdPosition = false
    },
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

          console.log("liste en Json", Object.entries(Json_xData))
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
        this.changeCdPlay(this.myAlbumModal);

        document.getElementById('cd-play').classList.add("rotate")
        //Ajouter la class rotate
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
      this.myAlbumPosX = item.Pos_X;
      this.myAlbumPosY = item.Pos_Y;
    },
    getImageUrl(album){
      if(album == "no_disque"){
        var nodisque = require("../../assets/photosAlbums/no_disque.png")
        return nodisque
      }else{
        var image = require("../../assets/photosAlbums/"+album.split(' ').join('_')+".jpg")
        return image
      }
    },
    toggleEditCdPosition(){
      this.showModalEditCdPosition = !this.showModalEditCdPosition
      this.myAlbumPosX2 = this.myAlbumPosY2 = null
    },
    saveCdPosition(e){
      e.preventDefault()
      console.log("avant ",this.myAlbumPosX, this.myAlbumPosY, this.myIdModal)
      console.log("aprezs",this.myAlbumPosX2, this.myAlbumPosY2)
      if(this.myAlbumPosX2 == null ||this.myAlbumPosY2 == null ){
        console.log("enregistrer null")
      }
      else{
        console.log("ok pour bdd")
        //requete vers bdd pour mettre a jour les coordonnées ?
        const postData = { requete: "editCdPosition", id: this.myIdModal, cdPositionX: this.myAlbumPosX2, cdPositionY: this.myAlbumPosY2};
        axios.post(this.$flaskUrl+"/editCdPosition", postData)
        .then(response => {
          console.log(response.status);
          this.myAlbumPosX = this.myAlbumPosX2
          this.myAlbumPosY = this.myAlbumPosY2
          this.listCd();
          // this.myAlbumPosX2 = this.myAlbumPosY2 = null
        }).catch(error => {
          this.errorMessage = error.message;
          console.error("There was an error!", error);
        });
      }

    },
    changeCdPlay(album){
      // let urll = this.getImageUrl(album)
      // console.log(urll)
      this.url = album
    },
    stopThisSong(){
      this.url = 'no_disque'
      document.getElementById('cd-play').classList.remove("rotate")
    },
    pauseThisSong(){
      document.getElementById('cd-play').classList.remove("rotate")
    },
    replayThisSong(){
      document.getElementById('cd-play').classList.add("rotate")
    }
  },
  computed: {


  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

.tableAlbum{
  margin-top: 0.5em;
  height: 20em;
  width: 100%;
  display: flex;
  justify-content: center;
}

.boxAlbum{
  border-radius: 50%;
  width: 140px;
  height: 140px;
  margin: 0.3em 0.6em 1.2em 0.6em;
  float: left;
  opacity: 0.85;
}.boxAlbum > p{
  font-size: 0px;
}.boxAlbum:hover > p{
  font-size: 3vh;
}
#pochette{
  border-radius: 50%;
}
.dot {
  height: 25px;
  width: 25px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
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


.imagePlay{
  height: 3em;
  width: 3em;
  cursor: pointer;
}
.classImageAlbum{
  height: 5em !important;
  width: 5em !important;
}
#ModalCdPosition{
  z-index: auto;
  /* height: 50vh; */
  /* width: 50vw; */
  top: 0;
}

.row-table{
  height: 5rem;
  width: 100vw;

}
.col-table{
  width: 20vw;
}
.background{
  background-color: red;
  border-radius: 10em;
  height: 5vh;
  width: 10vw;
}
.background2{
  background-color: blue;
  height: 5vh;
  width: 10vw;
}

#albums{
  height: 100%;
  width: 100%;
}

.btn-music{
  width: 20px;
  height: 20px;
}.btn-music:hover{
  cursor: pointer;
}


.height-100{
  height: 80vh;
  padding-top: 0px !important;
}

#centre-cd{
  background-color: #fff2dc;
  height: 34px;
  width: 35px;
  border-radius: 50%;
  margin-right: auto;
  margin-left: auto;
  border: solid 5px rgba(222, 222, 222, 0.352);
}

.image-cd{
  height: 270px;
  width: 270px;
  border-radius: 50%;
}

.rotate {
  animation: rotation 10s infinite linear;
}

@keyframes rotation {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
</style>

