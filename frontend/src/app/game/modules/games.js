import axios from 'axios'
import config from '@/config'

const state = {
  count: 0,
  params: {},
  sequence: [],
  index: null,
  next: null,
  previous: null
}

const mutations = {
  updateParams (state, payload) {
    let { params, count, sequence, direction, next, previous } = payload
    state.params = params
    state.next = next
    state.previous = previous
    state.count = count
    if (typeof direction === 'undefined') {
      direction = 'next'
    }
    let newSequence = []
    if (direction === 'next') {
      newSequence = state.sequence.concat(sequence)
    } else {
      newSequence = sequence.concat(state.sequence)
    }
    state.sequence = newSequence.filter((el, i, arr) => arr.indexOf(el) === i)
  },
  clearSequence (state) {
    state.sequence = []
  }
}

const actions = {
  async fetch ({ commit, dispatch }, params, direction) {
    try {
      const { data } = await axios.get(`${config.apiUrl}/games/`, { params })
      const { next, previous, count, results } = data
      const sequence = results.map((item) => item.id)
      commit('updateParams', { count, params, sequence, direction, next, previous })
      await dispatch('insertOrUpdate', {data: results})
      return results
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
