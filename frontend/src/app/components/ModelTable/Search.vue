<template>
  <v-slide-y-transition mode="out-in">
    <v-card class="ml-2">
      <v-card-title>
        <h3>Advanced Search</h3>
      </v-card-title>
      <v-divider></v-divider>
      <v-expansion-panel>
        <RangeInput v-for="field in numericFields"
        :field="field"
        :key="field.value"
        @update:params="updateParams($event)">
        </RangeInput>
      </v-expansion-panel>
    </v-card>
  </v-slide-y-transition>
</template>


<script>
import RangeInput from './RangeInput'

const props = {
  fields: {
    required: true,
    type: Array
  }
}

const components = {
  RangeInput
}

const computed = {
  numericFields () {
    return this.fields.filter(item => item.type === Number)
  },
  cleanParams () {
    const p = Object.assign({}, this.params)
    Object.keys(p).forEach((key) => {
      if (p[key] === null) {
        delete p[key]
      }
    })
    return p
  }
}

const methods = {
  updateParams (params) {
    this.$set(this, 'params', Object.assign({}, this.params, params))
  }
}

export default {
  name: 'search',
  computed,
  components,
  methods,
  props,
  watch: {
    params () {
      if (this.debounce !== null) {
        clearTimeout(this.debounce)
      }
      this.debounce = setTimeout(() => {
        this.$emit('update:params', this.cleanParams)
      }, 1000)
    }
  },
  data: () => ({
    debounce: null,
    params: {}
  })
}
</script>


<style scoped>
.advanced-search {
  margin: 30px;
}

</style>
