import Module from './module'

export default class Database {
  entities = []

  register (name, module) {
    this.entities.push({
      name,
      module
    })
  }
  modules () {
    return this.entities.reduce((modules, entity) => {
      modules[entity.name] = entity.module
      return modules
    }, {})
  }
  createModule (namespace) {
    return Module.create(namespace, this.modules())
  }
  registerStore (store) {
    this.store = store
  }
}
