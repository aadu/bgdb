<template>
  <v-navigation-drawer
    persistent
    :value="layout.sidebarVisible"
    app
    enable-resize-watcher
    fixed
    @input="handleInput"
    width="220"
  >
    <v-list class="pt-0" dense>
      <v-divider light></v-divider>
      <v-list-tile v-for="item in items" :key="item.title" :to="{name: item.route}">
        <v-list-tile-action>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>{{ item.title }}</v-list-tile-title>
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
      items: [
        {
          icon: 'apps',
          title: 'Board Games',
          route: 'games'
        },
        {
          icon: 'build',
          title: 'Mechanisms',
          route: 'mechanisms'
        }
      ]
    }
  }
}
</script>
