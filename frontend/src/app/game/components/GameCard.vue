<template>
  <v-card class="game">
    <v-card-media :src="game.image" height="400"></v-card-media>
    <v-card-title primary-title>
      <h1>{{ game.name }}</h1>
      <div v-html="game.description"></div>
    </v-card-title>
    <v-card-text>
      <GameStats :game="game"></GameStats>
    </v-card-text>
    <v-card-actions>
      <v-btn flat color="orange">Share</v-btn>
      <v-btn flat color="orange">Explore</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import GameStats from './GameStats'

const components = {
  GameStats
}

const props = {
  game: {
    required: true,
    type: Object
  }
}

export default {
  name: 'gameCard',
  components,
  props,
  data () {
    return {
    }
  }
}
</script>

<style scoped>
.game {
  background: grey%;
}

</style>


