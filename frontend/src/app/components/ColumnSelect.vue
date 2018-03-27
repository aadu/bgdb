<template>
<v-container>
    <v-btn icon flat @click.stop="visible = !visible">
      <v-icon>{{ icon }}</v-icon>
    </v-btn>
    <v-fade-transition mode="out-in">
      <v-card v-if="visible" class="column-select">
        <v-card-title>Select Columns</v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-checkbox
            v-for="field in fields"
            :label="field.text"
            :key="field.value"
            @change="$emit('update:list', $event)"
            :inputValue="list"
            :value="field.value">
            </v-checkbox>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="blue darken-1" flat @click.native="visible=false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-fade-transition>
    </v-container>
</template>


<script>
const props = {
  fields: {
    required: true,
    type: Array
  },
  list: {
    required: true,
    type: Array
  },
  icon: {
    default: 'list',
    type: String
  }
}

export default {
  name: 'columnSelect',
  props,
  data () {
    return {
      visible: false
    }
  }
}
</script>



<style scoped>
  .column-select {
    position: absolute;
    top: 70px;
    min-width: 200px;
    max-width: 650px;
  }
</style>
