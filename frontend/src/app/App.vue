<template>
  <v-app dark>
    <Sidebar></Sidebar>
    <Toolbar></Toolbar>
    <v-content fluid>
      <v-fade-transition mode="out-in">
          <router-view></router-view>
      </v-fade-transition>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import { Footer, Toolbar, Sidebar } from './layout'

const components = {
  Footer,
  Toolbar,
  Sidebar
}

export default {
  components,
  data () {
    return {}
  },
  name: 'App'
}
</script>

