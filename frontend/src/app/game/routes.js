import { GameList, GameDetail, MechanicList } from './components'

export default [
  {
    component: GameList,
    // path: '/games',
    path: '/',
    name: 'games',
    meta: { auth: false }
  },
  {
    component: GameDetail,
    path: '/game/:id',
    name: 'game',
    props: true,
    meta: { auth: false }
  },
  {
    component: MechanicList,
    path: '/mechanics',
    name: 'mechanics',
    meta: { auth: false }
  }
]
