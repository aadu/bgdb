<template>
  <ModelTable
    :fetch="fetch"
    :headers="headers"
    title="GamesList2"
    :count="count"
    @click="onClick($event)"
    :next="next"
    :previous="previous"
    @fetch="onFetch($event)"
    >
    <template slot="default" slot-scope="props">
      <td>{{ props.item.name }}</td>
      <td class="text-xs-right">{{ props.item.year_published }}</td>
      <td class="text-xs-right">{{ props.item.average_rating }}</td>
      <td class="text-xs-right">{{ props.item.num_votes }}</td>
      <td class="text-xs-right">{{ props.item.complexity }}</td>
      <td class="text-xs-right">{{ props.item.min_age }}</td>
      <td class="text-xs-right">{{ props.item.min_players }}</td>
      <td class="text-xs-right">{{ props.item.max_players }}</td>
      <td class="text-xs-right">{{ props.item.min_play_time }}</td>
      <td class="text-xs-right">{{ props.item.max_play_time }}</td>
    </template>
  </ModelTable>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { ModelTable } from '@/app/components'

const components = {
  ModelTable
}

const computed = {
  ...mapState(`entities/games`, [
    `count`, `next`, `previous`
  ])
}

const methods = {
  ...mapActions(`entities/games`, [
    `fetch`, `insertOrUpdate`
  ]),
  onClick (params) {
    this.$router.push({ name: 'game', ...params })
  },
  onFetch (results) {
    return this.insertOrUpdate({data: results})
  }
}

const headers = [
  {
    text: 'Name',
    align: 'left',
    value: 'name'
  },
  { text: 'Year Published', value: 'year_published', sortable: true },
  { text: 'Average Rating', value: 'average_rating', sortable: true },
  { text: 'Number of Ratings', value: 'num_votes', sortable: true },
  { text: 'Complexity', value: 'complexity', sortable: true },
  { text: 'Minimum Age', value: 'min_age', sortable: false },
  { text: 'Min Players', value: 'min_players', sortable: false },
  { text: 'Max Players', value: 'max_players', sortable: false },
  { text: 'Min Play Time', value: 'min_play_time', sortable: false },
  { text: 'Max Play Time', value: 'max_play_time', sortable: false }
]

export default {
  name: 'gamesList',
  methods,
  computed,
  components,
  data () {
    return {
      headers
    }
  }
}
</script>
