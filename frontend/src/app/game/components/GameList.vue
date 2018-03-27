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
