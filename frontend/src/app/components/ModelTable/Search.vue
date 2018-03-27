<template>
  <v-slide-y-transition mode="out-in">
    <v-card class="ml-2">
      <v-card-title>
        <h3>Advanced Search</h3>
      </v-card-title>
      <v-divider></v-divider>
      <v-expansion-panel>
        <v-expansion-panel-content v-for="field in numericFields" :key="field.value">
          <div slot="header">{{ field.text }} {{ display[field.value] }}</div>
          <v-card-text v-if="field.type === Number">
            <v-slider
              @input="onMinChange(field.value, $event)"
              :min="field.min || 0"
              :max="field.max || 100"
              hint="min"
              persistent-hint
              thumb-label
              v-model="params[field.value].min"
              ></v-slider>
            <v-slider
            @input="onMaxChange(field.value, $event)"
            :min="field.min || 0"
            :max="field.max || 100"
            hint="max"
            persistent-hint
            thumb-label
            v-model="params[field.value].max"
            ></v-slider>
          </v-card-text>
        </v-expansion-panel-content>
      </v-expansion-panel>
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

const computed = {
  display () {
    return Object.assign({}, ...Object.keys(this.params).map(item => ({[item]: this.getDisplay(item)})))
  },
  numericFields () {
    return this.fields.filter(item => item.type === Number)
  }
}

const methods = {
  onMinChange (key, value) {
    const max = this.params[key].max
    const field = this.fields.find(item => item.value === key)
    if (max > 0 && max > (field.min || 0) && max < value) {
      this.params[key].max = field.min || 0
    }
  },
  onMaxChange (key, value) {
    const min = this.params[key].min
    const field = this.fields.find(item => item.value === key)
    if (min > 0 && min > (field.min || 0) && min > value) {
      this.params[key].max = field.min || 0
    }
  },
  getDisplay (key) {
    const field = this.fields.find(item => item.value === key)
    const value = this.params[key]
    if (field.type === String) {
      return value
    } else if (field.type === Number) {
      const min = typeof value.min !== 'undefined' && value.min !== field.min ? value.min : null
      const max = typeof value.max !== 'undefined' && value.max !== field.min ? value.max : null
      if (min && max) {
        return `${min} - ${max}`
      } else if (min) {
        return `min: ${min}`
      } else if (max) {
        return `max: ${max}`
      }
    }
  }
}

export default {
  name: 'search',
  computed,
  methods,
  props,
  created () {
    this.fields.forEach(field => {
      let value = null
      if (field.type === Number) {
        value = {
          min: field.defaultMin || 0,
          max: field.defaultMax || 0
        }
      } else if (field.type === String) {
        value = field.default || ''
      } else if (field.type === Array) {
        value = field.default || []
      }
      this.$set(this.params, field.value, value)
    })
  },
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
