import axios from 'axios'
import config from '@/config'

const state = {
  count: 0,
  pagination: {
    page: 1,
    rowsPerPage: 500,
    sortBy: 'name',
    descending: false
  },
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
    const { data, params } = payload
    state.params = params
    state.next = data.next
    state.previous = data.previous
    state.count = data.count
    state.items = data.results
  }
}

const actions = {
  async fetch ({ commit, dispatch }, params) {
    try {
      const { data } = await axios.get(`${config.apiUrl}/mechanics/`, { params })
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
