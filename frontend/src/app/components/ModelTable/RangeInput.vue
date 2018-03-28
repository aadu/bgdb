<template>
  <v-expansion-panel-content>
    <div slot="header">{{ field.text }} {{ display }}</div>
    <v-card-text>
      <v-slider
        :min="min.min"
        :max="min.max"
        hint="min"
        persistent-hint
        thumb-label
        @input="onMin($event)"
        :value="min.value"
        ></v-slider>
      <v-slider
      :min="max.min"
      :max="max.max"
      hint="max"
      persistent-hint
      thumb-label
      @input="onMax($event)"
      :value="max.value"
      ></v-slider>
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
      [`${this.field.value}__lte`]: null,
      [`${this.field.value}__gte`]: null
    }
    if (this.maxValue) {
      p[`${this.field.value}__lte`] = this.maxValue
    }
    if (this.minValue) {
      p[`${this.field.value}__gte`] = this.minValue
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
      value: this.field.defaultMin || this.field.min || 0
    }
    const max = {
      min: this.field.min || 0,
      max: this.field.max || 100,
      value: this.field.defaultMax || this.field.max || 100
    }
    this.$set(this, 'min', min)
    this.$set(this, 'max', max)
    setTimeout(() => {
      this.loading = false
    }, 200)
  },
  data: () => ({
    min: {
      min: 0,
      max: 100,
      value: 0
    },
    max: {
      min: 0,
      max: 100,
      value: 0
    },
    debounce: null,
    loading: false
  })
}
</script>

<style scoped>
.advanced-search {
  margin: 30px;
}
</style>
