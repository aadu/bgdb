<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex xs12 md9>
      <v-card class="mr-1">
        <v-card-title>
            <slot name="title">
            <h2>{{ title }}</h2>
          </slot>
          <ColumnSelect
            v-if="columnSelect"
            :fields="fields"
            :list="list"
            @update:list="$emit('update:list', $event)">
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
            :value="searchInput"
            @input="onSearchChange($event)"
            @keyup.enter="fetchData"
          ></v-text-field>
        </v-card-title>
        <v-data-table
          class="elevation-1"
          :loading="loading"
          :headers="headers"
          :items="items"
          item-key="prop"
          :pagination="pagination"
          @update:pagination="onPageChange($event)"
          :search="search"
          :rows-per-page-items="rowsPerPage"
          :total-items="count"
          >
          <template slot="items" slot-scope="props">
            <tr @click="onClickRow(props.item.id, props.index)">
              <td v-for="field in headers" :key="field.prop">
                {{ log(props.item)}}
                <router-link
                  v-if="typeof field.link !== 'undefined'"
                  :to="{ name: field.link.name, params: { id: props.item.id }}"
                  >{{ field.formatter(props.item[field.prop]) }}</router-link>
                <span v-else-if="typeof field.component === 'undefined'">{{ field.formatter(props.item[field.prop]) }}</span>
                <component v-else :is="field.component" :value="field.formatter(props.item[field.prop])"></component>
              </td>
            </tr>
          </template>
        </v-data-table>
      </v-card>
    </v-flex>
    <v-flex md3 v-if="advancedSearch">
      <Search :fields="fields" @update:params="onUpdateParams($event)"></Search>
    </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import Search from './Search'
import ColumnSelect from './ColumnSelect'
import queryMixin from './mixins/query'

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
  },
  columnSelect: {
    default: true,
    type: Boolean
  }
}

const computed = {
  headers () {
    return this.fields.filter(item => this.list.includes(item.prop)).map(
      field => {
        return Object.assign({}, field, { value: field.prop, text: field.label })
      }
    )
  }
}

const methods = {
  log (event) {
    // console.log(event)
  },
  onSearchChange (text) {
    this.loading = true
    this.searchInput = text
    if (this.searchDebounce !== null) {
      clearTimeout(this.searchDebounce)
    }
    this.searchDebounce = setTimeout(() => {
      this.search = text
      console.log('onSearchChange')
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
    console.log('onPageChange')
    this.fetchData()
  },
  onUpdateParams (params) {
    this.loading = true
    if (this.paramDebounce !== null) {
      clearTimeout(this.paramDebounce)
    }
    this.paramDebounce = setTimeout(() => {
      this.params = params
      console.log('onUpdateParams')
      this.fetchData()
    }, 500)
  },
  fetchData () {
    this.$router.push({ query: this.queryParams })
  },
  loadData () {
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
  mixins: [queryMixin],
  mounted () {
    // this.loading = true
    // // if (this.initialPagination !== null) {
    // //   this.pagination = this.initialPagination
    // // }
    // this.loading = false
    this.selected = this.list
    document.addEventListener('keyup', this.keyUp)
    console.log('mounted')
    this.loadData()
  },
  props,
  data () {
    return {
      loading: true,
      search: null,
      searchInput: null,
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
      advancedSearch: true,
      paramDebounce: null,
      params: {}
    }
  },
  destroyed () {
    document.removeEventListener('keyup', this.keyUp)
  }
}
</script>
