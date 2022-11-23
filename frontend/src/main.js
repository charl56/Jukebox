import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'


Vue.config.productionTip = false
//// Fonctionnement en local :
// Vue.prototype.$flaskUrl = 'http://locahost:5025'
/// Fonctionnement pour image : 
// Vue.prototype.$flaskUrl = 'http://127.0.0.1:5025'
Vue.prototype.$flaskUrl = 'http://localhost:5025'


new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
