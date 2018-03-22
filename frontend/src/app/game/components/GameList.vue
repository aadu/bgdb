<template>
  <v-container class="ma3">
    <v-card>
      <v-card-title>
        Games
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
            <td class="text-xs-right">{{ props.item.year_published }}</td>
            <td class="text-xs-right">{{ props.item.min_age }}</td>
            <td class="text-xs-right">{{ props.item.min_players }}</td>
            <td class="text-xs-right">{{ props.item.max_players }}</td>
            <td class="text-xs-right">{{ props.item.min_play_time }}</td>
            <td class="text-xs-right">{{ props.item.max_play_time }}</td>
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

const name = 'gamesList'

const computed = {
  ...mapState(`entities/games`, [
    `count`, `params`, `items`, `pagination`
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
  ...mapActions(`entities/games`, [
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
    if (this.loading) {
      console.log('loading')
      return
    }
    this.$store.commit('entities/games/updatePagination', pagination)
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
  { text: 'Year Published', value: 'year_published', sortable: true },
  { text: 'Minimum Age', value: 'min_age', sortable: false },
  { text: 'Min Players', value: 'min_players', sortable: false },
  { text: 'Max Players', value: 'max_players', sortable: false },
  { text: 'Min Play Time', value: 'min_play_time', sortable: false },
  { text: 'Max Play Time', value: 'max_play_time', sortable: false }
]

export default {
  name,
  methods,
  computed,
  mounted () {
    // this.$store.commit('entities/games/clearSequence')
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
