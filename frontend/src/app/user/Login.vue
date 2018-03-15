
<template>
  <v-container fluid>
    <LoginForm class="ma-3"></LoginForm>
  </v-container>
</template>

<script>
import {default as LoginForm} from './Form'

const name = 'login'

const components = {
  LoginForm
}

export default {
  name,
  components
}
</script>
