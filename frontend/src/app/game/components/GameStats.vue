<template>
  <v-layout row wrap justify-space-between>
    <v-flex class="stat">
      <img src="@/assets/stat-player.png" alt="numPlayers">
      <p>{{ numPlayers }}</p>
    </v-flex>
    <v-flex class="stat">
      <img src="@/assets/stat-age.png" alt="ageRange">
      <p>{{ ageRange }}</p>
    </v-flex>
    <v-flex class="stat">
      <img src="@/assets/stat-length.png" alt="timeRange">
      <p>{{ timeRange }}</p>
    </v-flex>
  </v-layout>
</template>

<script>
const props = {
  game: {required: true}
}

const computed = {
  numPlayers () {
    if (this.game.max_players === 1) {
      return `1 player`
    }
    if (this.game.min_players === this.game.max_players) {
      return `${this.game.min_players} players`
    }
    if (!this.game.min_players && this.game.max_players) {
      return `up to ${this.game.max_players} players`
    }
    return `${this.game.min_players} - ${this.game.max_players} players`
  },
  ageRange () {
    return `age ${this.game.min_age}+`
  },
  timeRange () {
    return `${this.game.min_play_time} - ${this.game.max_play_time} minutes`
  }

}

export default {
  name: 'gameStats',
  computed,
  props
}
</script>



<style scoped>
.stat img {
  height: 64px;
  width: 64px;
}
.stat {
  font-size: 16px;
  color: gray;
}


</style>
