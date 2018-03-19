import axios from 'axios'
import config from '@/config'
import * as types from './types'

const initialState = {
  items: [],
  mechanics: [],
  categories: [],
  subcategories: [],
  tags: []
}

const mutations = {
  [types.SET_GAMES]: (state, items) => {
    state.items = items
  },
  [types.SET_MECHANICS]: (state, mechanics) => {
    state.mechanics = mechanics
  },
  [types.SET_CATEGORIES]: (state, categories) => {
    state.categories = categories
  },
  [types.SET_SUBCATEGORIES]: (state, subcategories) => {
    state.subcategories = subcategories
  },
  [types.SET_TAGS]: (state, tags) => {
    state.tags = tags
  }
}

const actions = {
  async getGames ({ commit }) {
    try {
      const { data } = await axios.get(config.gamesUrl)
      return commit(types.SET_GAMES, data.results)
    } catch (err) {
      return err
    }
  },
  async getMechanics ({ commit }) {
    try {
      const { data } = await axios.get(`${config.apiUrl}/mechanics/`)
      return commit(types.SET_MECHANICS, data.results)
    } catch (err) {
      return err
    }
  }

}

const getters = {
  games: state => {
    return state.items
  }
}

export default {
  state: initialState,
  mutations,
  getters,
  actions
}
