<template>
 <div class="text-xs-center">
    <v-bottom-sheet v-model="sheet" hide-overlay>
      <v-btn slot="activator" color="purple" dark>Click me</v-btn>
      <v-form>
        <v-text-field
          append-icon="search"
          label="Search"
          hide-details
          v-model="search"
        ></v-text-field>
      </v-form>
      <v-list>
        <v-subheader>Open in</v-subheader>
        <v-list-tile
          v-for="tile in tiles"
          :key="tile.title"
          @click="sheet = false"
        >
          <v-list-tile-title>{{ tile.title }}</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-bottom-sheet>
  </div>
</template>


<script>
export default {
  name: 'search',
  data () {
    return {
      search: '',
      sheet: false,
      tiles: [
        {title: "hello"},
        {title: "world"}
      ]

    }
  }
}
</script>
