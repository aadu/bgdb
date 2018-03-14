import * as types from './types'

const initialState = {
  sidebarVisible: true
}

const mutations = {
  [types.TOGGLE_SIDEBAR] (state) {
    state.sidebarVisible = !state.sidebarVisible
  }
}

const actions = {
  toggleSidebar: ({ commit }) => {
    commit(types.TOGGLE_SIDEBAR)
  }
}
const getters = {
  sidebarVisible: state => state.sidebarVisible
}

export default {
  state: initialState,
  getters,
  mutations,
  actions
}
