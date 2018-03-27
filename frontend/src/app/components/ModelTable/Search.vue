<template>
  <v-slide-y-transition mode="out-in">
    <v-card class="ml-2">
      <v-card-title>
        <h3>Advanced Search</h3>
      </v-card-title>
      <v-divider></v-divider>
      <v-expansion-panel>
        <v-expansion-panel-content>
          <div slot="header">Number of Ratings</div>
          <v-card-text>
            <v-slider :max="5000" hint="min" persistent-hint thumb-label v-model="params.num_votes.min"></v-slider>
            <v-slider :max="5000" hint="max" persistent-hint thumb-label v-model="params.num_votes.max"></v-slider>
          </v-card-text>
        </v-expansion-panel-content>

      </v-expansion-panel>

      <v-card-text>
        <v-container grid-list-md>
          <v-layout row wrap>
            <v-flex md9>
                <p>Number of Ratings</p>
                <v-slider :max="5000" hint="min" persistent-hint thumb-label v-model="params.num_votes.min"></v-slider>
                <v-slider :max="5000" hint="max" persistent-hint thumb-label v-model="params.num_votes.max"></v-slider>

            </v-flex>
            <v-flex md3>
              <v-text-field v-model="params.num_votes.max" type="number"></v-text-field>
            </v-flex>
            <v-flex md9>
              <v-text-field
                append-icon="search"
                label="Search"
                single-line
                hide-details
              ></v-text-field>
            </v-flex>
            <v-flex md9>
              <v-text-field
                  label="Title"
                  counter
              ></v-text-field>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card-text>

    </v-card>
  </v-slide-y-transition>
</template>


<script>

const props = {
  fields: {
    required: true,
    type: Array
  }
}

export default {
  name: 'search',
  props,
  data: () => ({
    visible: true,
    params: {}
  })
}
</script>


<style scoped>
.advanced-search {
  margin: 30px;
}

</style>
