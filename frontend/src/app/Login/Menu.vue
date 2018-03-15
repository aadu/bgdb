<template>
  <v-menu
    transition="slide-y-transition"
    bottom
    offset-y
    class="text-xs-center"
    :close-on-content-click="false"
    >
    <v-btn icon slot="activator">
      <v-icon>person</v-icon>
    </v-btn>
    <v-list>
      <v-list-tile @click="onLogin">
        <v-list-tile-title>Login</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
const name = 'loginMenu'

const methods = {
  onLogin () {
    this.$router.push({ name: 'login' })
  }
}
export default {
  name,
  methods
}
</script>

