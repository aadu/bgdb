import axios from 'axios'
import config from '@/config'
import * as types from './types'

const initialState = {
  items: [],
  count: 0,
  mechanics: [],
  categories: [],
  subcategories: [],
  tags: []
}

const mutations = {
  [types.SET_GAMES]: (state, { items, count }) => {
    state.items = items
    state.count = count
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

const formatFilterOptions = (pagination) => {
  const { sortBy, descending, page, rowsPerPage } = pagination
  const params = {}
  if (sortBy) {
    params['order_by'] = descending === true ? '-' + sortBy : sortBy
  }
  if (typeof page !== 'undefined') {
    params.page = page
  }
  if (typeof rowsPerPage !== 'undefined') {
    params.page_size = rowsPerPage
  }
  return params
}

const actions = {
  async getGames ({ commit, dispatch }, options) {
    const params = formatFilterOptions(options)
    console.log('params', params)
    try {
      const { data } = await axios.get(`${config.apiUrl}/games/`, {params})
      return commit(types.SET_GAMES, { items: data.results, count: data.count })
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
