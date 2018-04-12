import rootGetters from './rootGetters'
import rootActions from './rootActions'
import mutations from './mutations'
import subGetters from './subGetters'
import subActions from './subActions'

export default class Module {
  state () {
    return {
      $connection: '',
      $name: '',
      data: {}
    }
  }

  create (namespace, modules) {
    const tree = {
      namespaced: true,
      state: { $name: namespace },
      getters: rootGetters,
      actions: rootActions,
      mutations,
      modules: {}
    }

    return this.createTree(tree, namespace, modules)
  }

  createTree (tree, namespace, modules) {
    Object.keys(modules).forEach((name) => {
      const module = modules[name]

      tree.getters[name] = (_state, getters) => (wrap = true) => {
        return getters.query(name, wrap)
      }

      tree.modules[name] = {
        namespaced: true,
        state: {
          ...(typeof module.state === 'function' ? module.state() : module.state),
          ...this.state(),
          $connection: namespace,
          $name: name
        }
      }

      tree.modules[name]['getters'] = { ...subGetters, ...module.getters }
      tree.modules[name]['actions'] = { ...subActions, ...module.actions }
      tree.modules[name]['mutations'] = module.mutations || {}
    })
    return tree
  }
}
