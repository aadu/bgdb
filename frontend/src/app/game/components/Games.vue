<template>
  <v-container class="ma3">
    <v-data-table
      :headers="headers"
      :items="games"
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
import { mapActions, mapGetters } from 'vuex'
import Card from './Card'

const name = 'games'

const components = {
  Card
}

const computed = {
  ...mapGetters([
    `games`
  ])
}

const methods = {
  ...mapActions([
    `updateGames`
  ])
}

export default {
  name,
  methods,
  components,
  computed,
  data () {
    return {
      headers: [
        {
          text: 'Name',
          align: 'left',
          sortable: false,
          value: 'name'
        },
        { text: 'Minimum Age', value: 'min_age' },
        { text: 'Min Players', value: 'min_players' },
        { text: 'Max Players', value: 'max_players' },
        { text: 'Min Play Time', value: 'min_play_time' },
        { text: 'Max Play Time', value: 'max_play_time' }
      ],
    }
  },
  beforeMount () {
    this.updateGames(this)
  }
}
</script>
