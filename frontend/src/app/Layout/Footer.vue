<template>
  <v-footer :fixed="fixed" app>
    <span>&copy; 2017</span>
  </v-footer>
</template>

<script>
export default {
  data () {
    return {
      clipped: false,
      drawer: true,
      fixed: false,
      items: [{
        icon: 'bubble_chart',
        title: 'Board Game DataBase'
      }],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js',
      message: '',
      hints: '',
      fav: ''
    }
  },
  name: 'foot'
}
</script>
