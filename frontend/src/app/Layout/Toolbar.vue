<template>
  <v-toolbar
    app
    >
    <v-toolbar-side-icon @click.stop="toggleSidebar"></v-toolbar-side-icon>
    <v-toolbar-title>BGDB</v-toolbar-title>
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
const methods = {
  ...mapActions([
    `toggleSidebar`
  ])
}

const computed = {
  ...mapGetters([
    `sidebarVisible`
  ])
}

export default {
  name,
  methods,
  computed,
  components
}
</script>
