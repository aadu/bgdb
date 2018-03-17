<template>
  <v-container>
    <v-list>
      <v-list-tile v-for="(game, ix) in games" :key="ix">
        <v-list-tile-title v-text="game.name"></v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

const name = 'games'

const computed = {
  ...mapGetters([
    `games`
  ])
}
const methods = {
  ...mapActions([
    `updateGames`
  ])
}

export default {
  name,
  methods,
  computed
}
</script>
