import * as types from './types'

const initialState = {
  sidebarVisible: false,
  message: ''
}

const mutations = {
  [types.TOGGLE_SIDEBAR]: (state, visible) => {
    state.sidebarVisible = visible
  },
  [types.SET_MESSAGE]: (state, text) => {
    state.message = text
  }
}

const actions = {
  toggleSidebar: ({ commit }, visible) => {
    commit(types.TOGGLE_SIDEBAR, visible)
  },
  displayMessage: ({ commit }, text) => {
    commit(types.SET_MESSAGE, text)
  }
}

const getters = {
  message: state => {
    return state.message
  }
}

export default {
  state: initialState,
  mutations,
  getters,
  actions
}
