<template>
  <ModelTable
    :fetch="fetch"
    :fields="fields"
    :list="listView"
    @update:list="$store.commit('entities/games/updateList', $event)"
    title="Games"
    :count="count"
    @click="onClick($event)"
    :next="next"
    :previous="previous"
    @fetch="onFetch($event)"
    :initialPagination="initialPagination"
    >
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
    `count`, `next`, `previous`, `listView`
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

const fields = [
  {
    text: 'Name',
    align: 'left',
    value: 'name',
    type: String
  },
  { text: 'Year Published', value: 'year_published', sortable: true, type: Number, min: 1960, max: 2020 },
  { text: 'Average Rating', value: 'average_rating', sortable: true, type: Number, min: 0, max: 10, step: 0.2 },
  { text: 'Number of Ratings', value: 'num_votes', sortable: true, type: Number, min: 0, max: 1000, step: 10 },
  { text: 'Complexity', value: 'complexity', sortable: true, type: Number, min: 0, max: 5, step: 0.1 },
  { text: 'Minimum Age', value: 'min_age', sortable: false, type: Number, min: 4, max: 18 },
  { text: 'Min Players', value: 'min_players', sortable: false, type: Number, min: 1, max: 10 },
  { text: 'Max Players', value: 'max_players', sortable: false, type: Number, min: 1, max: 20 },
  { text: 'Min Play Time', value: 'min_play_time', sortable: false, type: Number, min: 1, max: 3 * 60, step: 15 },
  { text: 'Max Play Time', value: 'max_play_time', sortable: false, type: Number, min: 1, max: 12 * 60, step: 15 }
]

export default {
  name: 'gamesList',
  methods,
  computed,
  components,
  data () {
    return {
      fields,
      initialPagination: {
        page: 1,
        rowsPerPage: 50,
        sortBy: 'num_votes',
        descending: true
      }
    }
  }
}
</script>
