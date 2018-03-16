<template>
  <v-container fluid class="ma-3">
    <v-form width="200">
      <v-text-field
        label="Username"
        v-model="username"
        :error-messages="usernameErrors"
        :counter="24"
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
        label="First Name"
        v-model="fname"
        :error-messages="fnameErrors"
        :counter="64"
        @input="$v.fname.$touch()"
        @blur="$v.fname.$touch()"
        autocomplete="fname"
      ></v-text-field>
      <v-text-field
        label="Last Name"
        v-model="lname"
        :error-messages="lnameErrors"
        :counter="64"
        @input="$v.lname.$touch()"
        @blur="$v.lname.$touch()"
        autocomplete="lname"
      ></v-text-field>
      <v-text-field
        label="Password"
        hint="At least 8 characters"
        v-model="password"
        :error-messages="passwordErrors"
        @input="$v.password.$touch()"
        @blur="$v.password.$touch()"
        @keyup.enter="submit"
        required
        autocomplete="password"
        type="password"
      ></v-text-field>
      <v-btn @click="submit">submit</v-btn>
      <v-btn @click="clear">clear</v-btn>
    </v-form>
    <v-snackbar
      :top="true"
      :timeout="6000"
      v-model="snackbar"
    >
      {{ text }}
      <v-btn flat color="pink" @click.native="snackbar = false">Close</v-btn>
    </v-snackbar>
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
  submit () {
    this.$v.$touch()
    if (this.$v.$invalid) {
      this.text = 'Please fix the form'
      this.snackbar = true
    } else {
      this.login(this.user)
      this.text = 'Logged in succesfully'
      this.snackbar = true
      // this.$router.push({name: 'home'})
    }
  },
  clear () {
    this.$v.$reset()
    this.username = ''
    this.email = ''
    this.fname = ''
    this.lname = ''
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
  fnameErrors () {
    const errors = []
    if (!this.$v.fname.$dirty) return errors
    !this.$v.fname.maxLength && errors.push('First name must be at most 64 characters long')
    return errors
  },
  lnameErrors () {
    const errors = []
    if (!this.$v.lname.$dirty) return errors
    !this.$v.lname.maxLength && errors.push('User name must be at most 64 characters long')
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
    username: { required, maxLength: maxLength(24) },
    email: { required, email },
    fname: { maxLength: maxLength(64) },
    lname: { maxLength: maxLength(64) },
    password: { required }
  },
  methods,
  computed,
  data: () => ({
    username: '',
    email: '',
    fname: '',
    lname: '',
    password: '',
    text: '',
    snackbar: false
  })
}
</script>
