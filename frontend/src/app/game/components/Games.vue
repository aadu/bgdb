<template>
  <v-container class="ma3">
    <v-data-table
      :headers="headers"
      :items="games"
      :loading="loading"
      :pagination.sync="pagination"
      :total-items="game.count"
      hide-actions
      class="elevation-1"
      >
      <template slot="items" slot-scope="props">
        <td>{{ props.item.name }}</td>
        <td class="text-xs-right">{{ props.item.min_age }}</td>
        <td class="text-xs-right">{{ props.item.min_players }}</td>
        <td class="text-xs-right">{{ props.item.max_players }}</td>
        <td class="text-xs-right">{{ props.item.min_play_time }}</td>
        <td class="text-xs-right">{{ props.item.max_play_time }}</td>
        </template>
    </v-data-table>
  </v-container>
</template>

<script>
import { mapActions, mapGetters, mapState } from 'vuex'
import Card from './Card'

const name = 'games'

const components = {
  Card
}

const computed = {
  ...mapGetters([
    `games`
  ]),
  ...mapState([
    `game`
  ])
}

const methods = {
  ...mapActions([
    `getGames`
  ]),
  getDataFromApi () {
    this.loading = true
    this.getGames(this.pagination).then(() => {
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
  { text: 'Minimum Age', value: 'min_age', sortable: false },
  { text: 'Min Players', value: 'min_players', sortable: false },
  { text: 'Max Players', value: 'max_players', sortable: false },
  { text: 'Min Play Time', value: 'min_play_time', sortable: false },
  { text: 'Max Play Time', value: 'max_play_time', sortable: false }
]

export default {
  name,
  methods,
  components,
  computed,
  data () {
    return {
      loading: true,
      pagination: {},
      headers
    }
  },
  mounted () {
    this.getDataFromApi()
  },
  watch: {
    pagination: {
      handler () {
        this.getDataFromApi()
      }
    }
  }
}
</script>
