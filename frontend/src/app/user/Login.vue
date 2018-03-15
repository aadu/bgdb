<template>
  <v-container fluid class="ma-3">
    <v-form width="200">
      <v-text-field
        label="Name"
        v-model="name"
        :error-messages="nameErrors"
        :counter="10"
        @input="$v.name.$touch()"
        @blur="$v.name.$touch()"
        required
      ></v-text-field>
      <v-text-field
        label="E-mail"
        v-model="email"
        :error-messages="emailErrors"
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
        required
      ></v-text-field>
      <v-btn @click="submit">submit</v-btn>
      <v-btn @click="clear">clear</v-btn>
    </v-form>
  </v-container>
</template>

<style scoped>
  form {
    width: 640px;
  }
  body{
    background: #666 !important;
  }
</style>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'

const methods = {
  onSuccess (data) {
    this.$store.commit('setAuth', data)
    this.$router.replace('/')
  },
  submit () {
    this.$v.$touch()
  },
  clear () {
    this.$v.$reset()
    this.name = ''
    this.email = ''
    this.select = null
    this.checkbox = false
  }
}

const computed = {
  checkboxErrors () {
    const errors = []
    if (!this.$v.checkbox.$dirty) return errors
    !this.$v.checkbox.required && errors.push('You must agree to continue!')
    return errors
  },
  selectErrors () {
    const errors = []
    if (!this.$v.select.$dirty) return errors
    !this.$v.select.required && errors.push('Item is required')
    return errors
  },
  nameErrors () {
    const errors = []
    if (!this.$v.name.$dirty) return errors
    !this.$v.name.maxLength && errors.push('Name must be at most 10 characters long')
    !this.$v.name.required && errors.push('Name is required.')
    return errors
  },
  emailErrors () {
    const errors = []
    if (!this.$v.email.$dirty) return errors
    !this.$v.email.email && errors.push('Must be valid e-mail')
    !this.$v.email.required && errors.push('E-mail is required')
    return errors
  }
}

export default {
  mixins: [validationMixin],
  validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email }
  },
  methods,
  computed,
  data: () => ({
    name: '',
    email: ''
  })
}
</script>
