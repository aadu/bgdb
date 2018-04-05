export default class Registry {
  constructor (types = []) {
    this.registry = {}
    this.types = types
    this.types.forEach(type => {
      this.register(type)
    })
  }

  register (Field) {
    if (typeof Field === 'function') {
      this.types.push(Field)
      this.registry[Field.name] = []
      this[Field.name] = (prop, options = {}, validate = true) => {
        const field = new Field(prop, options, validate)
        this.registry[Field.name].push(field)
        return field
      }
      return
    }
    // Clone Field instances
    const name = Object.keys(Field)[0]
    this[name] = (prop, options = {}, validate = true) => {
      const field = Field[name].$clone(prop, options, validate)
      this.registry[Field[name].constructor.name].push(field)
      return field
    }
  }

  serialize (object) {
    const type = this.types.find((e) => {
      return e.name === object.constructor.name
    })
    if (typeof type === 'undefined') {
      throw Error(`type ${object.constructor.name} not registered`)
    }
    return JSON.stringify([type.name, Object.entries(object)])
  }

  deserialize (jstring) {
    let array = JSON.parse(jstring)
    let Type = this.types.find((e) => (e.name === array[0]))
    let object = new Type('', {}, false)
    array[1].map(e => {
      object[e[0]] = e[1]
    })
    return object
  }
}
