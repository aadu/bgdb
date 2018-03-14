<template>
  <v-navigation-drawer
    persistent
    :value="sidebarVisible"
    app
    enable-resize-watcher
    fixed
  >
    <v-list>
      <v-list-tile
        value="true"
        v-for="(item, i) in items"
        :key="i"
      >
        <v-list-tile-action>
          <v-icon v-html="item.icon"></v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title v-text="item.title"></v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import {mapGetters} from 'vuex'

const name = 'sidebar'
const computed = {
  ...mapGetters([
    `sidebarVisible`
  ])
}

export default {
  name,
  computed,
  data () {
    return {
      items: [{
        icon: 'bubble_chart',
        title: 'Board Game DataBase'
      }]
    }
  }
}
</script>
