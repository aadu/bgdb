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
        <v-list-tile-title>{{ user.isAuthenticated ? 'Logout' : 'Login' }}</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
import {mapActions, mapState} from 'vuex'

const name = 'loginMenu'

const computed = {
  ...mapState([
    `user`
  ])
}

const methods = {
  ...mapActions([
    `logout`
  ]),
  onLogin () {
    if (!this.user.isAuthenticated) {
      this.$router.push({ name: 'login' })
    } else {
      this.logout()
    }
  }
}
export default {
  name,
  computed,
  methods
}
</script>

