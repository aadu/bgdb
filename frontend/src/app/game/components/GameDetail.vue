<template>
  <v-slide-y-transition mode="out-in">
    <v-container fluid grid-list-md>
      <v-layout row wrap>
        <v-flex md8 d-flex>
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
        </v-flex>
        <v-flex md4>
          <v-card height="100%">
            <v-list>
              <v-list-tile>
              <v-list-tile-title>
                <h3>Links</h3>
              </v-list-tile-title>
              </v-list-tile>
              <v-divider></v-divider>
              <v-list-tile :href="game.url" color="grey" target="_blank">
                <v-list-tile-title>
                  BoardGameGeeks
                </v-list-tile-title>
              </v-list-tile>
              <v-list-tile :href="game.api_url" color="grey" target="_blank">
                <v-list-tile-title>
                  API
                </v-list-tile-title>
              </v-list-tile>
            </v-list>
          </v-card>
        </v-flex>

      </v-layout>
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

</style>
