import { mapState } from 'vuex'

const methods = {
  onRange ({ min, max, field }) {
    const params = {}
    if (typeof min !== 'undefined' && min !== null && min !== '') {
      params[`${field.prop}__lte`] = min
    }
    if (typeof max !== 'undefined' && max !== null && max !== '') {
      params[`${field.prop}__gte`] = max
    }
    this.fieldParams[field.prop] = params
  }

}

const computed = {
  ...mapState([
    `route`
  ]),
  query () {
    return this.route.query
  },
  searchFields () {
    return this.fields.filter((field) => (field.search === true))
  },
  searchQueryParams () {
    if (!this.search) {
      return {}
    }
    const params = {}
    this.searchFields.forEach((field) => {
      params[`${field.prop}__icontains`] = this.search
    })
    return params
  },
  pageQueryParams () {
    const { sortBy, descending, page, rowsPerPage } = this.pagination
    const params = {
      page,
      page_size: rowsPerPage,
      order_by: sortBy
    }
    if (sortBy && descending) {
      params['order_by'] = '-' + sortBy
    }
    Object.entries(params).forEach(([key, value]) => {
      if (typeof value === 'undefined' || value === null || value === '') {
        delete params[key]
      }
    })
    return params
  },
  fieldQueryParams () {
    return Object.assign({}, ...Object.values(this.fieldParams))
  },
  queryParams () {
    return { ...this.fieldQueryParams, ...this.searchQueryParams, ...this.pageQueryParams }
  },
  // reverse (query param to original data)
  // used to initialize values
  initSearch () {
    const searchKeys = this.searchFields.map((field) => (`${field.prop}__icontains`))
    const matches = Object.keys(this.query).filter(key => searchKeys.includes(key))
    if (matches.length) {
      return this.query[matches[0]]
    }
    return ''
  },
  initPagination () {
    const pagination = {
      page: this.query.page || this.init,
      rowsPerPage: this.query.page_size,
      sortBy: this.query.order_by
    }
    if (pagination.sortBy) {
      pagination.descending = pagination.sortBy.startsWith('-')
      pagination.sortBy = pagination.sortBy.replace(/^-/, '')
      return pagination
    }
    if (this.initialPagination !== null) {
      return this.initialPagination
    }
    return {
      page: 1,
      sortBy: null,
      rowsPerPage: 25,
      descending: false
    }
  }
}

export default {
  data () {
    return {
      fieldParams: {}
    }
  },
  computed,
  methods,
  mounted () {
    this.search = this.initSearch
    this.searchInput = this.initSearch
    this.pagination = this.initPagination
    console.log('initSearch=', this.initSearch)
  },
  watch: {
    queryParams () {
      console.log('queryParams1', this.queryParams)
    }
  }
}
