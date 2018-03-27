<template>
  <div class="text-xs-center">
    <v-menu
      offset-x
      :close-on-content-click="false"
      :nudge-width="200"
      v-model="visible"
    >
      <v-btn icon slot="activator">
        <v-icon color="grey">{{ icon }}</v-icon>
      </v-btn>
      <v-card>
        <v-list dense expand>
          <v-list-tile v-for="field in fields" :key="field.value">
            <v-list-tile-action>
              <v-checkbox
                @change="$emit('update:list', $event)"
                :inputValue="list"
                :value="field.value">
                </v-checkbox>
            </v-list-tile-action>
            <v-list-tile-title>{{ field.text }}</v-list-tile-title>
          </v-list-tile>
        </v-list>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn flat @click="visible = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-menu>
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

export default {
  name: 'columnSelect',
  props,
  mounted () {
    this.fields.forEach(field => {
      this.form[field.value] = {}
      if (typeof field.type === 'Number') {
        this.form[field.value].max = 0
        this.form[field.value].mix = 0
      }
    })

  },
  data () {
    return {
      visible: false
    }
  }
}
</script>
