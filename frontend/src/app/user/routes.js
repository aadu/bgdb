import { Login, Register } from './components'

export default [
  {
    component: Login,
    path: '/login',
    name: 'login',
    meta: { auth: false }
  },
  {
    component: Register,
    path: '/register',
    name: 'register',
    meta: { auth: false }
  }
]
