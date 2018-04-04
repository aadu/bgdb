export default class Query {

  constructor (state, entity) {
    this.state = state
    this.entity = entity
  }

  query (state, entity) {
    return new this(state, entity)
  }

  // DRF-compatible query params
  // pagination
  // lookup
  // sequence
}
