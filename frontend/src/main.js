import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import Vuetify from 'vuetify/lib'
import '@mdi/font/css/materialdesignicons.css' // Ensure you are using css-loader


Vue.config.productionTip = false
//// Fonctionnement en local :
// Vue.prototype.$flaskUrl = 'http://locahost:5025'
/// Fonctionnement pour image : 
// Vue.prototype.$flaskUrl = 'http://127.0.0.1:5025'
Vue.prototype.$flaskUrl = 'http://localhost:5025'

Vue.use(Vuetify)
export default new Vuetify({
  icons: {
    iconfont: 'mdiSvg',
  },
})

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
