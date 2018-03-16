<template>
  <div>
    <span v-if="user.isAuthenticated">{{ user.username }}</span>
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
      <v-list class="menu">
        <v-list-tile @click="onLogin" class="login">
          <v-list-tile-title>{{ user.isAuthenticated ? 'Logout' : 'Login' }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
  </div>
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

<style scoped>
.login {
  width: 160px;
}
.menu {
  padding: 0px;
  border-radius: 10px;
}
</style>
