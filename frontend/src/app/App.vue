<template>
  <v-app dark>
    <Sidebar></Sidebar>
    <Toolbar></Toolbar>
    <v-content>
    <transition name="fade" mode="out-in">
          <router-view/>
        </transition>
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
<style>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .3s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }
</style>

