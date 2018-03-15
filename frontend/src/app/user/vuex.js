import Vue from 'vue'
import Vuex from 'vuex'
import VueAxios from 'vue-axios'
import { VueAuthenticate } from 'vue-authenticate'
import axios from 'axios'
import * as types from './types'
import config from '@/config'

console.log(config)

Vue.use(Vuex)
Vue.use(VueAxios, axios)

const vueAuth = new VueAuthenticate(Vue.prototype.$http, {
  baseUrl: config.baseUrl,
  loginUrl: config.authUrl,
  registerUrl: config.registerUrl,
  storageNamespace: config.storageKey
})

const initialState = {
  isAuthenticated: false
}

const getters = {
  isAuthenticated () {
    return vueAuth.isAuthenticated()
  }
}

const mutations = {
  [types.AUTHENTICATE] (state, payload) {
    state.isAuthenticated = payload.isAuthenticated
  }
}

const actions = {
  login({ commit }, user, requestOptions) {
    vueAuth.login(user, requestOptions).then((response) => {
      commit(types.AUTHENTICATE, {
        isAuthenticated: vueAuth.isAuthenticated()
      })
    })
  }
}

export default {
  state: initialState,
  getters,
  mutations,
  actions
}
