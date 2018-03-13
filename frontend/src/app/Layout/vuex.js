import * as types from './types'

const initialState = {
  sideBarVisible: true
}

const mutations = {
  [types.TOGGLE_SIDEBAR_VISIBILITY] (state) {
    state.sideBarVisible = !state.sideBarVisible
  }
}
const actions = {
  toggleSidebar: ({ commit }) => {
    commit(types.TOGGLE_SIDEBAR_VISIBILITY)
  }
}
const getters = {
  sidebarVisible: state => state.sidebarVisible
}

export default {
  getters,
  mutations,
  actions,
  state: initialState
}
