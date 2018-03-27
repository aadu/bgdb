import axios from 'axios'
import config from '@/config'

const state = {
  count: 0,
  pagination: {
    page: 1,
    rowsPerPage: 50,
    sortBy: 'num_votes',
    descending: true
  },
  listView: ['name', 'year_published', 'average_rating', 'num_votes', 'complexity'],
  params: {},
  items: [],
  sequence: [],
  index: null,
  next: null,
  previous: null
}

const mutations = {
  updatePagination (state, { page, rowsPerPage, sortBy, descending }) {
    state.pagination = { page, rowsPerPage, sortBy, descending }
  },
  updateItems (state, payload) {
    console.log('FETCH')
    const { data, params } = payload
    state.params = params
    state.next = data.next
    state.previous = data.previous
    state.count = data.count
    state.items = data.results
    state.sequence = state.sequence.concat(data.results.map(item => item.id))
  },
  clearSequence (state) {
    state.sequence = []
  },
  updateList (state, payload) {
    state.listView = payload
  }
}

const actions = {
  async fetch ({ commit, dispatch }, params) {
    try {
      const { data } = await axios.get(`${config.apiUrl}/games/`, { params })
      commit('updateItems', { data, params })
      return data.results
    } catch (err) {
      console.log(err)
      dispatch('displayMessage', err)
      return err
    }
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
