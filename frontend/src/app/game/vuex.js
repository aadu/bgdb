import config from '@/config'
import * as types from './types'

const initialState = {
  list: []
}

const mutations = {
  [types.SET_GAMES]: (state, games) => {
    state.list = games
  }
}

const actions = {
  updateGames: ({ commit }, context) => {
    return context.$http.get(config.gamesUrl).then(({ data }) => {
      commit(types.SET_GAMES, data.results)
    }).catch((err) => {
      return err
    })
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
