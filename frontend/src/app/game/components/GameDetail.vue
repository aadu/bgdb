<template>
  <v-slide-y-transition mode="out-in">
    <div class="game">
      <h2>{{ game.name }}</h2>
      <div v-html="game.description"></div>
    </div>
  </v-slide-y-transition>
</template>

<script>
const name = 'gameCard'

const props = {
  game: { required: true }
}

export default {
  name,
  props
}
</script>

<style scoped>
  .game {
    background-color: rgb(109, 31, 31);
    border-radius: 15px;
    padding: 15px;
    margin: 30px;
    box-shadow: ghostwhite;
  }
  .game h2 {
    font-size: 20px;
    margin-bottom: 15px;
  }

  .game:hover {
    background-color: rgb(91, 9, 9);
  }
  .game ::selection {
    background-color: rgba(255, 255, 0, 0.728);
  }

  .game div::first-letter {
    font-size: 200%
  }

  .game div::first-line {
    font-weight: bold;
  }

</style>
