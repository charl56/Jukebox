<template>
    <v-row class="divHeader">
        <v-col md="3" sm="3">
        </v-col>        
        <v-col md="6" sm="9">
            <h1 class="appTitle">Jukebox</h1>
        </v-col>
        <v-col offset-md="0" class="colAddSong" md="3" sm="3">
            <v-dialog v-model="dialogAdd" transition="dialog-top-transition" max-width="600px">
                <template v-slot:activator="{ on, attrs }">
                    <v-btn id="buttonAdd" class="" fab dark v-bind="attrs" v-on="on">
                        <v-icon dark>+</v-icon>
                    </v-btn>
                </template>                   
                <v-card id="card-add">
                    <v-card-title>
                        <span class="text-h5 text-white">Ajouter un album</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                                <form class="" id="formAdd" @submit="saveSong" method="post">
                                    <div class="">                            
                                        <input class="input-add" v-model="myArtist" type="text" placeholder="Artiste" required>
                                    </div>                                     
                                    <div class="">                            
                                        <input class="input-add" v-model="myAlbum" type="text" placeholder="Album" required>
                                    </div>                                     
                                    <div class="">                            
                                        <input class="input-add" v-model="mySongNb" type="number" placeholder="Nombre de sons" required>
                                    </div>                                     
                                    <div class="btn-container">
                                        <input class="input-button" id="cancel-button"  type="button" value="Annuler" v-on:click="dialogAdd = false">
                                        <input class="input-button" id="submit-button" type="submit" value="Ajouter" >
                                    </div>     
                                </form> 
                        </v-container>
                    </v-card-text>
                </v-card>
            </v-dialog>
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
            dialogAdd: false,
            dialogSettings: false,
            myAlbum: '',
            myArtist: '',
            mySongNb:'',
            rules: [
                value => !value || value.size < 2000000 || 'Album picture\'s size should be less than 2 MB!',
            ],
            imageAlbum: null
        }
    },
    methods:{
        // onFileSelector(e){
        //     this.imageAlbum = e.target.file[0]
        // },
        // onUpload(){

        // },
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
        saveSong(e) {
            e.preventDefault();
            // Ferme le popup
            this.dialogAdd = false;
            // Requete axios vers DB
            this.saveSongDB();
            // Vide les variables
            this.myAlbum = this.myArtist = this.mySongNb = null;
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
        },
        savePlacement(){
            // console.log("OK")
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
    height: auto;
}

.appTitle{
    font-size: xx-large;
    text-align: center;
    color: #B1BAC7;
}

.colAddSong{
    text-align: center;
}
#buttonAdd{
    background-color: #B1BAC7 !important;
    color: white;
    margin-top: auto;
    margin-bottom: auto;
    height: 50px;
    width: 50px;
}
#card-add{
    background-color: #B1BAC7;
    height: auto;
    width: auto;
    border-radius: 10px;
    border: 10px solid #B1BAC7;
}
.input-add{
    background-color: white;
    border-radius: 5px;
    padding: 5px;
    margin: 5px;
}.input-add:focus{
    font-size: 1rem;
}
.input-button{
    width: 5rem;
    background-color: wheat;
    border-radius: 10px;
    margin: 10px;
}
#cancel-button{
    background-color: #A7001E;
}#cancel-button:hover{
    background-color: #955149;
}
#submit-button{
    background-color: #7AA95C;
}#submit-button:hover{
    background-color: #a6e6a6;
}
.btn-container{
    margin: 10px;

}
</style>
  
  