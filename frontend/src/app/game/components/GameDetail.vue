<template>
  <v-slide-y-transition mode="out-in">
    <v-container>
      <v-card class="game">
        <v-card-media :src="game.image" height="400"></v-card-media>
        <v-card-title primary-title>
          <h1>{{ game.name }}</h1>
          <div v-html="game.description"></div>
        </v-card-title>
        <v-card-actions>
          <v-btn flat color="orange">Share</v-btn>
          <v-btn flat color="orange">Explore</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-slide-y-transition>
</template>

<script>
import { mapActions, mapState } from 'vuex'

const name = 'gameCard'

const methods = {
  ...mapActions([
    `getGameDetail`
  ])
}

const computed = {
  ...mapState({
    game: state => state.game.detail

  })
}

export default {
  name,
  computed,
  methods,
  data () {
    return {
      loading: false
    }
  },
  mounted () {
    this.loading = true
    this.getGameDetail(this.$route.params.id).then(() => {
      this.loading = false
    })
  }
}
</script>

<style scoped>
  .game {
    width: 60%;
    flex: 2, 2, auto;
  }


</style>
