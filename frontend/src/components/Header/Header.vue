<template>
    <v-row class="divHeader">
        <v-col offset-md="3" md="6" sm="9">
            <h1 class="appTitle">{{ msg }}</h1>
          <i class="fa-solid fa-pause"></i>
        </v-col>
        <v-col  offset-md="0" class="colAddSong" md="3" sm="3">
            <v-row justify="center">
                <v-dialog v-model="dialog" transition="dialog-top-transition" max-width="600px">
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn id="buttonAdd" class="" fab dark v-bind="attrs" v-on="on">
                            <v-icon dark>+</v-icon>
                        </v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                            <span class="text-h5">Ajouter un album</span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col cols="12" sm="6" md="4" >
                                        <v-text-field v-model="myArtist" label="Artiste">
                                        </v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6" md="4">
                                        <v-text-field v-model="myAlbum" label="Nom de l'album">
                                        </v-text-field>
                                    </v-col>
                                    <v-col cols="12" sm="6" md="4" >
                                        <v-text-field v-model="mySongNb" label="Nombre de son">
                                        </v-text-field>
                                    </v-col>    
                                    <v-col cols="12" sm="6" md="4" >
                                        <v-file-input show-size accept="image/jpg" label="Pochette de l'album" :rules="rules" truncate-length="15" ></v-file-input>
                                    </v-col>  
                                </v-row>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn color="blue darken-1" text @click="dialog = false" >
                                Close
                            </v-btn>
                            <v-btn color="blue darken-1" text @click="saveSong" >
                                Save
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-row>
        </v-col>
        <!-- <v-progress-linear id="loadingBar" buffer-value="00" indeterminate color="cyan"></v-progress-linear> -->
    
    </v-row>
</template>
  

<script>  
import axios from 'axios';

  export default {
    name: 'AppHeader',
    props: {
      msg: String
    },
    created(){
        this.$root.$refs.Header = this;
    },
    mounted(){ // Lance la fonction au chargement de la page
      console.log("start")
      this.loadingBar();
      // document.getElementById("test1").style.color = "blue";
    },
    data () {
        return {
            dialog: false,
            myAlbum: '',
            myArtist: '',
            mySongNb:'',
            rules: [
                value => !value || value.size < 2000000 || 'Album picture\'s size should be less than 2 MB!',
            ],
        }
    },
    methods:{
        loadingBar(visibility) {
            if(visibility == "visible"){
                // document.getElementById("my_canvas_tree").style.visibility = "visible";
                document.getElementById("idTable").style.visibility = "visible";
                
            }
            else{
                // document.getElementById("my_canvas_tree").style.visibility = "visible";
                document.getElementById("idTable").style.visibility = "visible";
            }
        },
        saveSong() {
            console.log("add song")
            console.log(this.myAlbum, this.mySongNb, Number.isInteger(parseInt(this.mySongNb)));  
            if(this.myAlbum == '' || this.myArtist == '' || this.mySongNb == '') {
                alert("Toutes les cases doivent être remplies")
            }
            else if (Number.isInteger(parseInt(this.mySongNb)) == false){
                alert("Le nombre de son doit être en chiffre")
            }
            else{  
                this.dialog = false;
                this.saveSongDB();
                this.myAlbum = this.myArtist = this.mySongNb = null;
            }
        },
        async saveSongDB() {
            console.log("SaveSongDb")            
            const postData = { requete: "SaveSongDb", myAlbum: this.myAlbum, myArtist: this.myArtist, mySongNb: this.mySongNb };
            await axios.post(this.$flaskUrl+"/SaveSongDb", postData)
             // await axios.post(this.$flaskUrl+"/listCd")
             .then(response => {
             console.log(response.status);   
            })
            .catch(error => {
            console.error("There was an error!", error);
            });
            this.$root.$refs.Table.listCd();
        }        
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style >

.divHeader{
    background-color: #2A4E62;
    box-shadow: 0px 2px 5px #001C2F;
    margin: 0 !important;
    height: 4em;
}

.appTitle{
    text-align: center;
    color: #B1BAC7;
}

.colAddSong{
    text-align: center;
    margin-top: 0.2em;
}
#buttonAdd{
    background-color: #B1BAC7 !important;
    color: white;
}
</style>
  
  