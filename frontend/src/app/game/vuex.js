import axios from 'axios'
import config from '@/config'
import * as types from './types'

const initialState = {
  items: [],
  lookup: {},
  count: 0,
  params: {},
  next: null,
  previous: null,
  detail: {},
  mechanics: [],
  categories: [],
  subcategories: [],
  tags: []
}

const mutations = {
  [types.SET_GAMES]: (state, { data, params }) => {
    state.items = data.results
    state.count = data.count
    state.next = data.next
    state.previous = data.previous
    state.params = params
    state.lookup = Object.assign(...state.items.map((item, ix) => ({ [item.id]: ix })))
  },
  [types.SET_GAME_DETAIL]: (state, data) => {
    state.detail = data
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
  async getGames ({ commit, dispatch }, params) {
    try {
      // console.log('fetch', params)
      const { data } = await axios.get(`${config.apiUrl}/games/`, {params})
      return commit(types.SET_GAMES, { data, params })
    } catch (err) {
      console.log(err)
      dispatch('displayMessage', err)
      return err
    }
  },
  async getGameDetail ({ commit, dispatch }, id) {
    try {
      const { data } = await axios.get(`${config.apiUrl}/games/${id}/`)
      return commit(types.SET_GAME_DETAIL, data)
    } catch (err) {
      console.log(err)
      dispatch('displayMessage', err)
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
