<template>
  <v-app>
    <Sidebar></Sidebar>
    <Toolbar></Toolbar>
    <v-content>
      <router-view/>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import { Footer, Toolbar, Sidebar } from './Layout'

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
