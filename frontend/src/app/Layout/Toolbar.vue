<template>
  <v-toolbar
    app
    >
    <v-toolbar-side-icon @click.stop="onToggle"></v-toolbar-side-icon>
    <v-toolbar-title @click="onTitle">BGDB</v-toolbar-title>
    <v-spacer></v-spacer>
    <LoginMenu></LoginMenu>
  </v-toolbar>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import { Menu as LoginMenu } from '../Login'

const name = 'toolbar'
const components = {
  LoginMenu
}
const computed = {
  ...mapGetters([
    `sidebarVisible`
  ])
}
const methods = {
  ...mapActions([
    `toggleSidebar`
  ]),
  onToggle () {
    this.toggleSidebar(!this.sidebarVisible)
  },
  onTitle () {
    this.$router.push({name: 'home'})
  }
}

export default {
  name,
  methods,
  components,
  computed
}
</script>
