<template>
  <div>
    <v-btn icon @click.stop="visible = !visible">
      <v-icon color="grey">{{ icon }}</v-icon>
    </v-btn>
    <v-fade-transition mode="out-in">
      <div v-if="visible" id="column-select-modal">
        <v-card class="column-select">
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
        </div>
    </v-fade-transition>
  </div>
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
    default: 'view_column',
    type: String
  }
}

const methods = {
  onClick (event) {
    const el = document.getElementById('column-select-modal')
    if (event.target === el) {
      this.visible = false
    }
  }
}

export default {
  name: 'columnSelect',
  methods,
  props,
  data () {
    return {
      visible: false
    }
  },
  mounted () {
    document.addEventListener('click', this.onClick)
  },
  destroyed () {
    document.removeEventListener('click', this.onClick)
  }
}
</script>


<style scoped>
  .column-select {
    position: absolute;
    top: 70px;
    min-width: 200px;
    max-width: 650px;
    z-index: 2;
  }
  #column-select-modal {
    position: absolute;
    z-index: 1; /* Sit on top */
    left: 0;
    top: 0;
    width: 100%; /* Full width */
    height: 100%; /* Full height */
    overflow: auto; /* Enable scroll if needed */
    background-color: rgb(0,0,0); /* Fallback color */
    background-color: rgba(0,0,0,0.05); /* Black w/ opacity */
    -webkit-animation-name: fadeIn; /* Fade in the background */
    -webkit-animation-duration: 0.4s;
    animation-name: fadeIn;
    animation-duration: 0.4s
}

</style>
