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
import { mapActions, mapState } from 'vuex'
import { LoginMenu } from '@/app/user/components'

const name = 'toolbar'
const components = {
  LoginMenu
}
const computed = {
  ...mapState([
    `layout`
  ])
}
const methods = {
  ...mapActions([
    `toggleSidebar`
  ]),
  onToggle () {
    this.toggleSidebar(!this.layout.sidebarVisible)
  },
  onTitle () {
    this.$router.push({path: '/'})
  }
}

export default {
  name,
  methods,
  components,
  computed
}
</script>
