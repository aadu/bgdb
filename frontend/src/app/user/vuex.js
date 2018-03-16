import Vue from 'vue'
import Vuex from 'vuex'
import VueAxios from 'vue-axios'
import { VueAuthenticate } from 'vue-authenticate'
import axios from 'axios'
import * as types from './types'
import config from '@/config'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

const vueAuth = new VueAuthenticate(Vue.prototype.$http, {
  baseUrl: config.baseUrl,
  loginUrl: config.authUrl,
  registerUrl: config.registerUrl,
  storageNamespace: config.storageKey
})

const initialState = {
  username: null,
  isAuthenticated: false
}

const mutations = {
  [types.CHECK_AUTH] (state, payload) {
    state.isAuthenticated = payload.isAuthenticated
    state.username = payload.username
  }
}

const actions = {
  login ({ commit }, user, requestOptions) {
    return vueAuth.login(user, requestOptions).then((response) => {
      commit(types.CHECK_AUTH, {
        isAuthenticated: vueAuth.isAuthenticated(),
        username: user.username
      })
      return response
    })
  },
  logout ({ commit }) {
    return vueAuth.logout().then((response) => {
      if (!vueAuth.isAuthenticated()) {
        commit(types.CHECK_AUTH, {
          isAuthenticated: false,
          username: null
        })
        return response
      }
    })
  },
  register ({ commit }, user, requestOptions) {
    return vueAuth.register(user).then((response) => {
      commit(types.CHECK_AUTH, {
        isAuthenticated: vueAuth.isAuthenticated(),
        username: user.username
      })
      return response
    })
  }
}

export default {
  state: initialState,
  mutations,
  actions
}
