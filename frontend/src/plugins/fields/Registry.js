export default class Registry {
  constructor (types = []) {
    this.registry = {}
    this.types = types
    this.types.forEach(type => {
      this.register(type)
    })
  }

  register (Field) {
    this.types.push(Field)
    this.registry[Field.name] = Field
    this[Field.name] = (prop, options = {}, validate = true) => {
      return new Field(prop, options, validate)
    }
  }

  serialize (object) {
    const lookup = Object.entries(this.registry).find((e) => {
      return e[1].name === object.constructor.name
    })
    if (typeof lookup === 'undefined') {
      throw Error(`type ${object.constructor.name} not registered`)
    }
    return JSON.stringify([lookup[0], Object.entries(object)])
  }

  deserialize (jstring) {
    let array = JSON.parse(jstring)
    let Type = this.registry[array[0]]
    let object = new Type('', {}, false)
    array[1].map(e => {
      object[e[0]] = e[1]
    })
    return object
  }
}
