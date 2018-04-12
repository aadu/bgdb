<template>
  <v-expansion-panel-content>
    <div slot="header">{{ field.label }} {{ display }}</div>
    <v-card-text>
      <v-container fluid grid-list-sm>
        <v-layout row wrap>
          <v-flex d-flex xs5>
            <v-text-field
              type="number"
              label="Min"
              :clearable="true"
              single-line
              :value="min.value"
              @input="onMin($event)"
              :step="step"
              :min="min.min"
              :max="min.max">
            </v-text-field>
          </v-flex>
          <v-flex d-flex xs2>
          </v-flex>
          <v-flex d-flex xs5>
            <v-text-field
              type="number"
              label="Max"
              :clearable="true"
              single-line
              :value="max.value"
              @input="onMax($event)"
              :step="step"
              :min="max.min"
              :max="max.max">
            </v-text-field>
          </v-flex>
        </v-layout>
      </v-container>
    </v-card-text>
  </v-expansion-panel-content>
</template>

<script>
const props = {
  field: {
    required: true,
    type: Object
  }
}

const computed = {
  minValue () {
    const value = this.min.value
    if (value === this.min.min) {
      return null
    }
    this.$emit('update:min', value)
    return value
  },
  maxValue () {
    const value = this.max.value
    if (value === this.max.max) {
      return null
    }
    this.$emit('update:max', value)
    return value
  },
  display () {
    if (this.minValue && this.maxValue) {
      return `${this.minValue} - ${this.maxValue}`
    } else if (this.minValue) {
      return `min: ${this.minValue}`
    } else if (this.maxValue) {
      return `max: ${this.maxValue}`
    }
  },
  params () {
    const p = {
      [`${this.field.prop}__lte`]: null,
      [`${this.field.prop}__gte`]: null
    }
    if (this.maxValue) {
      p[`${this.field.prop}__lte`] = this.maxValue
    }
    if (this.minValue) {
      p[`${this.field.prop}__gte`] = this.minValue
    }
    return p
  }
}

const methods = {
  onMin (value) {
    this.min.value = value
    if (value > this.max.value && this.maxValue) {
      this.max.value = this.max.min
    }
  },
  onMax (value) {
    this.max.value = value
    if (this.debounce !== null) {
      clearTimeout(this.debounce)
    }
    this.debounce = setTimeout(() => {
      if (value < this.min.value && this.minValue) {
        this.min.value = this.min.min
      }
    }, 300)
  }
}

export default {
  name: 'rangeInput',
  computed,
  methods,
  props,
  watch: {
    params () {
      if (!this.loading) {
        this.$emit('update:params', this.params)
      }
    }
  },
  mounted () {
    this.loading = true
    const min = {
      min: this.field.min || 0,
      max: this.field.max || 100,
      value: undefined
    }
    const max = {
      min: this.field.min || 0,
      max: this.field.max || 100,
      value: undefined
    }
    this.$set(this, 'min', min)
    this.$set(this, 'max', max)
    this.step = this.field.step || 0
    setTimeout(() => {
      this.loading = false
    }, 200)
  },
  data: () => ({
    min: {
      min: 0,
      max: 100,
      value: undefined
    },
    max: {
      min: 0,
      max: 100,
      value: undefined
    },
    debounce: null,
    loading: false,
    step: 1
  })
}
</script>

<style scoped>
.advanced-search {
  margin: 30px;
}
</style>
