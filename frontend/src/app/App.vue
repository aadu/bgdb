<template>
  <v-app>
    <Sidebar></Sidebar>
    <Toolbar></Toolbar>
    <v-content>
      <v-fade-transition mode="out-in">
          <router-view :key="$route.fullPath"></router-view>
      </v-fade-transition>
      <Notifier></Notifier>
    </v-content>
    <Footer></Footer>
  </v-app>
</template>

<script>
import { Footer, Notifier, Toolbar, Sidebar } from './layout/components'

const components = {
  Footer,
  Notifier,
  Toolbar,
  Sidebar
}

export default {
  name: 'App',
  components
}
</script>

