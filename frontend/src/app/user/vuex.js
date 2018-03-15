import Vue from 'vue'
import Vuex from 'vuex'
import VueAxios from 'vue-axios'
import { VueAuthenticate } from 'vue-authenticate'
import axios from 'axios'
import * as types from './types'
import config from '@/config'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

// function Auth () {}

// Object.defineProperty(Auth.prototype, 'vueAuth', {
//   get: function () {
//     const vueAuth = new VueAuthenticate(Vue.prototype.$http, {
//       baseUrl: config.api
//     })
//     Object.defineProperty(this, 'vueAuth', {
//       value: vueAuth
//     })

//     return vueAuth
//   }
// })

// const auth = new Auth()

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
  [types.AUTHENTICATE] (state, payload) {
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
