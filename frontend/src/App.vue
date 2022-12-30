<template>
  <v-app>

    <!-- <div id="app"> -->
    <div>
      <Header />
      <Table />
      <v-col md="6" sm="6">
        <!-- <FractaleTree /> -->
      </v-col>
      <v-col md="6" sm="6">
        <!-- <FractaleNGon /> -->
      </v-col>
    </div>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import Table from './components/Table/Table.vue'
import Header from './components/Header/Header.vue'
// import FractaleTree from './components/Fractale/FractaleTree.vue'
// import FractaleNGon from './components/Fractale/FractaleNGon.vue'

import './style.css'

export default {
  name: 'App',
  components: {
    Table,
    Header,
    // FractaleTree,
    // FractaleNGon
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #FFF2DC;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
</style>
