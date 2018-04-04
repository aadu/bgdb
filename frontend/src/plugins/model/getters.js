import { Query } from './query'

const rootGetters = {
  query: (state) => (entity, wrap) => {
    return Query.query(state, entity, wrap)
  },
  all: (state) => (entity, wrap) => {
    return Query.all(state, entity, wrap)
  },
  find: (state) => (entity, id, wrap) => {
    return Query.find(state, entity, id, wrap)
  }
}

export default rootGetters
