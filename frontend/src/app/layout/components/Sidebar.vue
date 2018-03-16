<template>
  <v-navigation-drawer
    persistent
    :value="layout.sidebarVisible"
    app
    enable-resize-watcher
    fixed
    @input="handleInput"
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
import {mapState, mapActions} from 'vuex'

const name = 'sidebar'
const computed = {
  ...mapState([
    `layout`
  ])
}

const methods = {
  ...mapActions([
    `toggleSidebar`
  ]),
  handleInput (event) {
    this.toggleSidebar(event)
  }
}

export default {
  name,
  computed,
  methods,
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
