import { normCase } from './utils'

export default class Field {
  constructor (prop, options = {}, validate = true) {
    this.prop = prop

    Object.defineProperty(this, '_options', {
      enumerable: false,
      writable: false,
      value: Object.assign({}, options)
    })

    if (typeof options.label === 'undefined') {
      options.label = normCase(prop)
    }

    Object.assign(this, this.$defaults, options)
    if (validate === true) {
      this.$validate()
    }

    if (typeof this.class === 'undefined') {
      this.class = this.constructor.name.replace('Field', '')
    }

    // Ensure custom Field classes include defaults in override
    if (typeof this.protoIncluded === 'undefined') {
      throw Error('Field $defaults override should extend __proto__.$defaults')
    }
    delete this.protoIncluded
    this.$init()
  }

  $clone (prop, options = {}, validate = true) {
    return new this.constructor(prop || this.prop, Object.assign({}, this._options, options), validate)
  }

  $repr () {
    const opts = Object.keys(this._options).length > 0 ? `, ${JSON.stringify(this._options)}` : ''
    return `${this.constructor.name}("${this.prop}"${opts})`
  }

  toJSON () {
    return [this.constructor.name, Object.entries(this)]
  }

  toString () {
    return this.$repr()
  }

  [Symbol.toPrimitive] (hint) {
    if (hint === 'default' || hint === 'string') {
      return this.$repr()
    }
  }

  $init () { }

  get $defaults () {
    return {
      protoIncluded: true,
      sortable: false,
      required: false,
      readonly: false,
      except: '',
      minWidth: 120,
      formatter: v => v
    }
  }

  get $requiredArguments () {
    return [
      'label', 'prop'
    ]
  }

  $validate () {
    this.$requiredArguments.forEach((prop) => {
      if (typeof this[prop] === 'undefined') {
        throw Error(`${prop} is a required argument for field "${this.label}"`)
      }
    })
  }
}
