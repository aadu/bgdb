import Vue from 'vue'
import Vuex from 'vuex'
import VueAxios from 'vue-axios'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import { sync } from 'vuex-router-sync'
import { vuex } from '@/app'
import router from './router'
import config from '@/config'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

const modules = { ...vuex }

const store = new Vuex.Store({
  plugins: [
    createPersistedState({
      key: config.storageKey,
      paths: ['ux']
    })
  ],
  modules
})

sync(store, router)

export default store
