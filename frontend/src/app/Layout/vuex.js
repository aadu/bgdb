import * as types from './types'

const initialState = {
  sidebarVisible: false
}

const mutations = {
  [types.TOGGLE_SIDEBAR] (state, visible) {
    state.sidebarVisible = visible
  }
}

const actions = {
  toggleSidebar: ({ commit }, visible) => {
    commit(types.TOGGLE_SIDEBAR, visible)
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
