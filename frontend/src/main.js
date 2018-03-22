// The Vue build version to load with the `import` command
// (Offline-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vuetify from 'vuetify'
// import * as Offline from 'offline-plugin/runtime'
import 'vuetify/dist/vuetify.min.css'
import { App } from './app'
import router from './router'
import store from './store'

Vue.use(VueAxios, axios)
Vue.use(Vuetify)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store
})

// Offline.install({
//   onUpdating: () => {
//     console.log('SW Event:', 'onUpdating')
//   },
//   onUpdateReady: () => {
//     console.log('SW Event:', 'onUpdateReady')
//     // Tells to new SW to take control immediately
//     Offline.applyUpdate()
//   },
//   onUpdated: () => {
//     console.log('SW Event:', 'onUpdated')
//     // Reload the webpage to load into the new version
//     window.location.reload()
//   },
//   onUpdateFailed: () => {
//     console.log('SW Event:', 'onUpdateFailed')
//   }
// })
