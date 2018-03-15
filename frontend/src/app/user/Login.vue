<template>
  <v-container fluid class="ma-3">
    <v-form width="200">
      <v-text-field
        label="Username"
        v-model="username"
        :error-messages="usernameErrors"
        :counter="10"
        @input="$v.username.$touch()"
        @blur="$v.username.$touch()"
        autocomplete="username"
        required
      ></v-text-field>
      <v-text-field
        label="E-mail"
        v-model="email"
        :error-messages="emailErrors"
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
        autocomplete="email"
        required
      ></v-text-field>
      <v-text-field
        label="Password"
        hint="At least 8 characters"
        v-model="password"
        :error-messages="passwordErrors"
        @input="$v.password.$touch()"
        @blur="$v.password.$touch()"
        required
        autocomplete="password"
        type="password"
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
import { mapActions } from 'vuex'

const methods = {
  ...mapActions(
    [`login`]
  ),
  onSuccess (data) {
    this.$store.commit('setAuth', data)
    this.$router.replace('/')
  },
  submit () {
    this.$v.$touch()
    this.login(this.user)
  },
  clear () {
    this.$v.$reset()
    this.username = ''
    this.email = ''
    this.password = ''
  }
}

const computed = {
  passwordErrors () {
    const errors = []
    if (!this.$v.password.$dirty) return errors
    !this.$v.password.required && errors.push('Password is required')
    return errors
  },
  usernameErrors () {
    const errors = []
    if (!this.$v.username.$dirty) return errors
    !this.$v.username.maxLength && errors.push('User name must be at most 10 characters long')
    !this.$v.username.required && errors.push('User name is required.')
    return errors
  },
  emailErrors () {
    const errors = []
    if (!this.$v.email.$dirty) return errors
    !this.$v.email.email && errors.push('Must be valid e-mail')
    !this.$v.email.required && errors.push('E-mail is required')
    return errors
  },
  user () {
    return {
      username: this.username,
      password: this.password
    }
  }
}

export default {
  mixins: [validationMixin],
  validations: {
    username: { required, maxLength: maxLength(24) },
    email: { required, email },
    password: { required }
  },
  methods,
  computed,
  data: () => ({
    username: '',
    email: '',
    password: ''
  })
}
</script>
