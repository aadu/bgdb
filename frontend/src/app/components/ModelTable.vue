<template>
  <v-container class="ma3">
    <v-card>
      <v-card-title>
        {{ title }}
        <v-spacer></v-spacer>
        <v-text-field
          append-icon="search"
          label="Search"
          single-line
          hide-details
          v-model="search"
          @input="onSearchChange($event)"
          @keyup.enter="fetchData"
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="items"
        :loading="loading"
        :pagination="pagination"
        @update:pagination="onPageChange($event)"
        :search="search"
        :rows-per-page-items="rowsPerPage"
        :total-items="count"
        class="elevation-1"
        >
        <template slot="items" slot-scope="props">
          <tr @click="onClickRow(props.item.id, props.index)">
            <slot :item="props.item"></slot>
          </tr>
        </template>
        <v-alert slot="no-results" :value="true" color="error" icon="warning">
          Your search for "{{ search }}" found no results.
        </v-alert>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
const props = {
  title: {
    default: '',
    type: String
  },
  headers: {
    required: true,
    type: Array
  },
  fetch: {
    required: true,
    type: Function
  },
  rowsPerPage: {
    type: Array,
    default: () => [25, 50, 100, 500]
  },
  count: {
    default: 0,
    type: Number
  },
  next: {
    default: null
  },
  previous: {
    default: null
  }
}

const computed = {
  queryParams () {
    const { sortBy, descending, page, rowsPerPage } = this.pagination
    const output = {}
    if (sortBy) {
      output['order_by'] = descending === true ? '-' + sortBy : sortBy
    }
    if (typeof page !== 'undefined') {
      output.page = page
    }
    if (typeof rowsPerPage !== 'undefined') {
      output.page_size = rowsPerPage
    }
    if (this.search) {
      output.name__icontains = this.search
    }
    return output
  }
}

const methods = {
  onSearchChange (text) {
    this.loading = true
    if (this.searchDebounce !== null) {
      clearTimeout(this.searchDebounce)
    }
    this.searchDebounce = setTimeout(() => {
      this.search = text
      this.fetchData()
    }, 500)
  },
  rowIndex (index) {
    return index + ((this.pagination.page - 1) * this.pagination.rowsPerPage)
  },
  onClickRow (id, index) {
    this.$emit('click', { params: { id }, query: { index: this.rowIndex(index) } })
  },
  onPageChange ({ page, rowsPerPage, sortBy, descending }) {
    if (this.loading) {
      return
    }
    this.pagination = { page, rowsPerPage, sortBy, descending }
    this.fetchData()
  },
  fetchData () {
    this.loading = true
    this.fetch(this.queryParams).then((results) => {
      this.loading = false
      this.items = results
      this.$emit('fetch', results)
    })
  },
  keyUp ({ keyCode }) {
    if (keyCode !== 39 && keyCode !== 37) {
      return
    }
    const nextPage = Object.assign({}, this.pagination)
    // right
    if (keyCode === 39 && this.next) {
      nextPage.page = nextPage.page + 1
    } else if (keyCode === 37 && this.previous) {
      nextPage.page = nextPage.page - 1
    }
    // left
    this.onPageChange(nextPage)
  }
}

export default {
  name: 'modelTable',
  methods,
  computed,
  mounted () {
    document.addEventListener('keyup', this.keyUp)
    this.fetchData()
  },
  props,
  data () {
    return {
      loading: true,
      search: '',
      searchDebounce: null,
      pagination: {
        page: 1,
        sortBy: null,
        rowsPerPage: 25,
        descending: false
      },
      items: []
    }
  },
  destroyed () {
    document.removeEventListener('keyup', this.keyUp)
  }
}
</script>
