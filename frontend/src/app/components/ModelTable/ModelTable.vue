<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 md9>
      <v-card class="mr-1">
        <v-card-title>
          <h2>{{ title }}</h2>
          <ColumnSelect
            :list="list"
            @update:list="$emit('update:list', $event)"
            :fields="fields">
          </ColumnSelect>
          <v-btn icon @click.prevent.native="advancedSearch = !advancedSearch">
            <v-icon color="grey">keyboard_arrow_right</v-icon>
          </v-btn>
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
              <td v-for="field in headers" :key="field.value">{{ props.item[field.value] }}</td>
            </tr>
          </template>
        </v-data-table>
      </v-card>
    </v-flex>
    <v-flex md3 v-if="advancedSearch">
      <Search :fields="fields"></Search>
    </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Search from './Search'
import ColumnSelect from './ColumnSelect'

const components = {
  Search,
  ColumnSelect
}

const props = {
  title: {
    default: '',
    type: String
  },
  fields: {
    required: true,
    type: Array
  },
  fetch: {
    required: true,
    type: Function
  },
  list: {
    required: true,
    type: Array
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
  },
  initialPagination: {
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
  },
  headers () {
    return this.fields.filter(item => this.list.includes(item.value))
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
  components,
  computed,
  mounted () {
    this.loading = true
    if (this.initialPagination !== null) {
      this.pagination = this.initialPagination
    }
    this.loading = false
    this.selected = this.list
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
      items: [],
      columnToggle: false,
      selected: [],
      advancedSearch: true
    }
  },
  destroyed () {
    document.removeEventListener('keyup', this.keyUp)
  }
}
</script>
