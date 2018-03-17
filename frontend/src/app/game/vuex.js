import * as types from './types'

const initialState = {
  list: [
    { name: 'HELLO' },
    { name: 'HELLO2' }
  ]
}

const mutations = {
  [types.SET_GAMES]: (state, games) => {
    state.list = games
  }
}

const actions = {
  updateGames: ({ commit }, text) => {
    commit(types.SET_GAMES, text)
  }
}

const getters = {
  games: state => {
    return state.list
  }
}

export default {
  state: initialState,
  mutations,
  getters,
  actions
}
