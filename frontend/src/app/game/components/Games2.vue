<template>
  <v-container class="ma3">
    <ul>
      <Card v-for="(game, ix) in games" :key="ix" :game="game" class="ma3"></Card>
    </ul>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Card from './Card'

const name = 'games'

const components = {
  Card
}

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
  components,
  computed,
  beforeMount () {
    this.updateGames(this)
  }
}
</script>
