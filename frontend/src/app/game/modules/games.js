import axios from 'axios'
import config from '@/config'

const state = {
  count: 0,
  params: {},
  sequence: [],
  index: null
}

const mutations = {
  updateParams (state, { params, count, sequence, direction }) {
    state.params = params
    state.count = count
    if (typeof direction === 'undefined') {
      direction = 'next'
    }
    if (direction === 'next') {
      state.sequence = state.sequence.concat(sequence)
    } else {
      state.sequence = sequence.concat(state.sequence)
    }
  },
  clearSequence (state) {
    state.sequence = []
  }
}

const actions = {
  async fetch ({ commit, dispatch }, params, direction) {
    try {
      const { data } = await axios.get(`${config.apiUrl}/games/`, { params })
      const sequence = data.results.map((item) => item.id)
      commit('updateParams', { count: data.count, params, sequence, direction })
      await dispatch('insertOrUpdate', {data: data.results})
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
