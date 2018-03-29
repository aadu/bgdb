<template>
  <ModelTable
    :fetch="fetch"
    :fields="fields"
    :list="listView"
    @update:list="$store.commit('entities/mechanics/updateList', $event)"
    title="Game Mechanics"
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
  ...mapState(`entities/mechanics`, [
    `count`, `next`, `previous`, `listView`
  ])
}

const methods = {
  ...mapActions(`entities/mechanics`, [
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
  { text: 'Description', value: 'description', type: String }
]

export default {
  name: 'mechanicsList',
  methods,
  computed,
  components,
  data () {
    return {
      fields,
      initialPagination: {
        page: 1,
        rowsPerPage: 200,
        sortBy: 'name',
        descending: true
      }
    }
  }
}
</script>
