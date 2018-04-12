export default (database, options = {}) => {
  const namespace = options.namespace || 'entities'

  return (store) => {
    store.registerModule(namespace, database.createModule(namespace))
    database.registerStore(store)
    database.registerNamespace(namespace)
  }
}
