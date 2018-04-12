import axios from 'axios'
import config from '@/config'
import Fields from '@/plugins/fields'

  //   { text: 'Year Published', value: 'year_published', sortable: true, type: Number, min: 1980, max: 2020, step: 5 },
// { text: 'Average Rating', value: 'average_rating', sortable: true, type: Number, min: 0, max: 10, step: 0.2 },
// { text: 'Number of Ratings', value: 'num_votes', sortable: true, type: Number, min: 0, max: 1000, step: 10 },
// { text: 'Complexity', value: 'complexity', sortable: true, type: Number, min: 0, max: 5, step: 0.1 },
// { text: 'Minimum Age', value: 'min_age', sortable: false, type: Number, min: 4, max: 18, step: 1 },
// { text: 'Min Players', value: 'min_players', sortable: false, type: Number, min: 1, max: 10, step: 1 },
// { text: 'Max Players', value: 'max_players', sortable: false, type: Number, min: 1, max: 20, step: 1 },
// { text: 'Min Play Time', value: 'min_play_time', sortable: false, type: Number, min: 1, max: 3 * 60, step: 15 },
// { text: 'Max Play Time', value: 'max_play_time', sortable: false, type: Number, min: 1, max: 12 * 60, step: 15 }

const fields = [
  new Fields.StringField('name', { sortable: true }),
  new Fields.StringField('description')
]

const state = {
  fields,
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

const getters = {
  find: (state) => (id) => {
    return state.items.find(item => item.id === id)
  }
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
  getters,
  state,
  mutations,
  actions
}
