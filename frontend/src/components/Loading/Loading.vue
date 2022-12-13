<template>
    <v-row class="rowLoading">
        <div class="divLoading">
            <canvas id="myLoading" ></canvas>
        </div>
    </v-row>
</template>

<script>
export default {
    name: 'AppLoading',
    created(){
    this.$root.$refs.Loading = this;
    },
    mounted(){ // Lance la fonction au chargement de la page
           
    },
    data () {
        return {
        myCanvas: '',
        }
    },
    methods:{
        async playThisSong(){
        },
    },
    computed: {

    }
}
</script>

<style>
.divLoading{
    background-color: white;
    width: 100%;
    height: 100%;
}
</style>