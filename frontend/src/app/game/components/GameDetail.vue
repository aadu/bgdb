<template>
  <v-slide-y-transition mode="out-in">
    <v-container fluid grid-list-md v-if="!loading">
      <v-layout row wrap>
        <v-flex md8 d-flex>
          <GameCard :game="game"></GameCard>
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
import { mapActions, mapState, mapGetters } from 'vuex'
import GameCard from './GameCard'
const name = 'gameDetail'

const components = {
  GameCard
}

const props = {
  id: {required: true}
}

const methods = {
  ...mapActions(`game/games`, [
    `fetch`
  ]),
  getPrevious () {
    if (this.index === 0) {
      const self = this
      const params = this.params
      params['page'] = params['page'] - 1
      return this.fetch(params, 'previous').then((results) => {
        self.$router.push({
          name: 'game',
          params: { id: self.sequence[results.length - 1] },
          query: {index: results.length - 1}
        })
      })
    }
    this.$router.push({
      name: 'game',
      params: { id: this.sequence[this.index - 1] },
      query: {index: this.index - 1}
    })
  },
  getNext () {
    if (this.index + 1 === this.sequence.length) {
      const self = this
      const params = this.params
      params['page'] = params['page'] + 1
      return this.fetch(params, 'next').then(() => {
        self.$router.push({
          name: 'game',
          params: { id: self.sequence[this.index + 1] },
          query: { index: this.index + 1 }
        })
      })
    }
    this.$router.push({
      name: 'game',
      params: { id: this.sequence[this.index + 1] },
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
  ...mapState(`game/games`, [
    `sequence`, `next`, `previous`, `data`, `params`
  ]),
  ...mapGetters(`game/games`, [
    `find`
  ]),
  nextItem () {
    if (typeof this.index === 'undefined') {
      return false
    }
    if (this.index + 1 < this.sequence.length) {
      return true
    }
    if (this.index + 1 === this.sequence.length && this.next) {
      return true
    }
    return false
  },
  previousItem () {
    if (typeof this.index === 'undefined') {
      return false
    }
    if (this.sequence.length > this.index - 1 && this.index - 1 >= 0) {
      return true
    }
    if (this.sequence === 0 && this.previous) {
      return true
    }
    return false
  }
}

export default {
  name,
  components,
  computed,
  methods,
  props,
  data () {
    return {
      loading: false,
      index: null,
      game: {}
    }
  },
  mounted () {
    document.addEventListener('keyup', this.keyUp)
    this.index = this.$route.query.index
    this.game = this.find(this.id)
    if (!this.game) {
      this.loading = true
      this.fetch({id: this.id}).then((results) => {
        this.game = results[0]
        this.loading = false
      })
    }
  },
  destroyed () {
    document.removeEventListener('keyup', this.keyUp)
  }
}
</script>

