<template>
  <div class="game">
    <h2>{{ game.name }}</h2>
    <div v-html="game.description"></div>
  </div>
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
    background-color: darkslategrey;
    border-radius: 15px;
    padding: 15px;
    margin: 30px;
  }
  .game h2 {
    font-size: 20px;
    margin-bottom: 15px;
  }
</style>
