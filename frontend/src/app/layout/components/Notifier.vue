
<template>
  <v-snackbar
    :top="true"
    :timeout="3000"
    v-model="snackbar"
  >
    {{ message }}
    <v-btn flat color="pink" @click.native="snackbar = false">Close</v-btn>
  </v-snackbar>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

const computed = {
  ...mapGetters([
    `message`
  ])
}

const methods = {
  ...mapActions([
    `displayMessage`
  ]),
  wait: ms => new Promise((resolve, reject) => {
    setTimeout(resolve, ms)
  })
}

const watch = {
  message (text) {
    if (text !== '') {
      this.snackbar = true
    }
  },
  snackbar (visible) {
    if (!visible) {
      this.wait(500).then(() => {
        this.displayMessage('')
      })
    }
  }
}

export default {
  name: 'Notifier',
  methods,
  computed,
  data () {
    return {
      snackbar: false
    }
  },
  watch
}
</script>

