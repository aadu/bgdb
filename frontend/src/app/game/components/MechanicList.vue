<template>
  <v-container class="ma3">
    <v-card>
      <v-card-title>
        Mechanics
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
        :rows-per-page-items="[25, 50, 100, 500]"
        :total-items="count"
        class="elevation-1"
        >
        <template slot="items" slot-scope="props">
          <tr @click="onClickRow(props.item.id, props.index)">
            <td>{{ props.item.name }}</td>
            <td class="text-xs-right" v-html="props.item.description"></td>
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
import { mapActions, mapState } from 'vuex'

const name = 'mechanicsList'

const computed = {
  ...mapState(`entities/mechanics`, [
    `count`, `params`, `items`, `pagination`, `next`, `previous`
  ]),
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
  ...mapActions(`entities/mechanics`, [
    `fetch`, `insertOrUpdate`
  ]),
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
  onClickRow (id, index) {
    this.$router.push({ name: 'game', params: { id }, query: { index: this.rowIndex(index) } })
  },
  onPageChange (pagination) {
    console.log(pagination)
    if (this.loading) {
      console.log('loading')
      return
    }
    this.$store.commit('entities/mechanics/updatePagination', pagination)
    this.fetchData()
  },
  fetchData () {
    this.loading = true
    this.fetch(this.queryParams).then((results) => {
      this.loading = false
      return this.insertOrUpdate({data: results})
    })
  },
  rowIndex (index) {
    return index + ((this.pagination.page - 1) * this.pagination.rowsPerPage)
  }
}

const headers = [
  {
    text: 'Name',
    align: 'left',
    value: 'name'
  },
  { text: 'Description', value: 'description', align: 'left', sortable: false }
]

export default {
  name,
  methods,
  computed,
  mounted () {
    this.fetchData()
  },
  data () {
    return {
      loading: true,
      search: '',
      searchDebounce: null,
      headers
    }
  }
}
</script>
