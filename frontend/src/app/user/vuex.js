import Vue from 'vue'
import VueAuthenticate from 'vue-authenticate'

import * as types from './types'
import config from '@/config'

const vueAuth = new VueAuthenticate(Vue.prototype.$http, {
  baseUrl: config.api
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
  [types.AUTHENTICATE](state, payload) {
    state.isAuthenticated = payload.isAuthenticated
  }
}

const actions = {
  login (context, payload) {
    vueAuth.login(payload.user, payload.requestOptions).then((response) => {
      context.commit(types.AUTHENTICATE, {
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
