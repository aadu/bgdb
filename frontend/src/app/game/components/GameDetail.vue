<template>
  <v-slide-y-transition mode="out-in">
    <v-container fluid grid-list-md v-if="!loading">
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
              <v-spacer></v-spacer>
              <v-list-tile v-if="previousItem || nextItem">
                <v-flex row wrap>
                <v-btn
                  v-if="previousItem"
                  @click="getPrevious"
                >
                Previous
                </v-btn>
                <v-btn v-if="nextItem" @click="getNext">Next</v-btn>
                </v-flex>
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

const props = {
  id: {required: true}
}

const methods = {
  ...mapActions([
    `getGameDetail`,
    `getGames`
  ]),
  getPrevious () {
    if (this.index === 0) {
      const self = this
      const params = this.params
      params['page'] = params['page'] - 1
      return this.getGames(params).then(() => {
        self.$router.push({
          name: 'game',
          params: { id: self.items[self.items.length - 1].id },
          query: {index: self.items.length - 1}
        })
      })
    }
    this.$router.push({
      name: 'game',
      params: { id: this.items[this.index - 1].id },
      query: {index: this.index - 1}
    })
  },
  getNext () {
    if (this.index + 1 === this.items.length) {
      const self = this
      const params = this.params
      params['page'] = params['page'] + 1
      return this.getGames(params).then(() => {
        self.$router.push({
          name: 'game',
          params: { id: self.items[0].id },
          query: { index: 0 }
        })
      })
    }
    this.$router.push({
      name: 'game',
      params: { id: this.items[this.index + 1].id },
      query: {index: this.index + 1}
    })
  },
  keyUp ({ keyCode }) {
    if (keyCode === 39 && this.nextItem) {
      // right
      this.getNext()
    } else if (keyCode === 37 && this.previousItem) {
      // left
      this.getPrevious()
    }
  }
}

const computed = {
  ...mapState({
    game: state => state.game.detail,
    items: state => state.game.items,
    next: state => state.game.next,
    previous: state => state.game.previous,
    params: state => state.game.params
  }),
  nextItem () {
    if (typeof this.index === 'undefined') {
      return false
    }
    if (this.index + 1 < this.items.length) {
      return true
    }
    if (this.index + 1 === this.items.length && this.next) {
      return true
    }
    return false
  },
  previousItem () {
    if (typeof this.index === 'undefined') {
      return false
    }
    if (this.items.length > this.index - 1 && this.index - 1 >= 0) {
      return true
    }
    if (this.index === 0 && this.previous) {
      return true
    }
    return false
  }
}

export default {
  name,
  computed,
  methods,
  props,
  data () {
    return {
      loading: false,
      index: null
    }
  },
  mounted () {
    document.addEventListener('keyup', this.keyUp)
    this.index = this.$route.query.index
    this.loading = true
    this.getGameDetail(this.id).then(() => {
      this.loading = false
    })
  },
  destroyed () {
    document.removeEventListener('keyup', this.keyUp)
  }
}
</script>

<style scoped>

</style>
