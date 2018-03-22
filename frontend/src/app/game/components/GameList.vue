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
        :pagination.sync="pagination"
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
    `count`, `params`, `sequence`
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
    `fetch`
  ]),
  onSearchChange (text) {
    if (this.searchDebounce !== null) {
      clearTimeout(this.searchDebounce)
    }
    this.searchDebounce = setTimeout(() => {
      this.search = text
      this.fetchData()
    }, 500)
  },
  onClickRow (id) {
    this.$router.push({ name: 'game', params: { id }, query: { index: this.sequence.findIndex(id) } })
  },
  onPageChange (pagination) {
    if (this.count === 0) {
      return
    }
    if (!pagination.initialized) {
      this.pagination.initialized = true
      return
    }
    this.fetchData()
  },
  fetchData () {
    this.loading = true
    this.fetch(this.queryParams).then((items) => {
      this.items = items
      this.loading = false
    })
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
    // console.log(this)
    this.$store.commit('entities/games/clearSequence')
    this.fetchData()
  },
  data () {
    return {
      loading: true,
      items: [],
      pagination: {
        page: 1,
        rowsPerPage: 25,
        totalItems: 0,
        sortBy: 'name',
        descending: false,
        initialized: false
      },
      search: '',
      searchDebounce: null,
      headers
    }
  }
}
</script>
