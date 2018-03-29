import axios from 'axios'
import config from '@/config'

const state = {
  count: 0,
  pagination: {
    page: 1,
    rowsPerPage: 100,
    sortBy: 'name',
    descending: true
  },
  listView: ['name', 'description'],
  params: {},
  items: [],
  sequence: [],
  index: null,
  next: null,
  previous: null
}

const getters = {
  items (state) {
    return state.items
  }
}

const mutations = {
  updatePagination (state, { page, rowsPerPage, sortBy, descending }) {
    state.pagination = { page, rowsPerPage, sortBy, descending }
  },
  updateItems (state, payload) {
    console.log('FETCH mechanics')
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
  async fetch ({ commit, dispatch, getters }, params) {
    // const items = getters.items
    // if (items.length) {
    //   return items
    // }
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
  getters,
  state,
  mutations,
  actions
}
