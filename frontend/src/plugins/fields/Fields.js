import { normCase } from './utils'
import Registry from './Registry'

class Field {
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

    // Ensure custom Field classes include defaults in override
    if (typeof this.protoIncluded === 'undefined') {
      throw Error('Field $defaults override should extend __proto__.$defaults')
    }
    delete this.protoIncluded

    this.$init()
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

  $init () {}

  get $defaults () {
    return {
      protoIncluded: true,
      default: undefined,
      sortable: false,
      value: undefined,
      required: false,
      readonly: false,
      except: '',
      minWidth: 120
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

  //   { text: 'Year Published', value: 'year_published', sortable: true, type: Number, min: 1980, max: 2020, step: 5 },
// { text: 'Average Rating', value: 'average_rating', sortable: true, type: Number, min: 0, max: 10, step: 0.2 },
// { text: 'Number of Ratings', value: 'num_votes', sortable: true, type: Number, min: 0, max: 1000, step: 10 },
// { text: 'Complexity', value: 'complexity', sortable: true, type: Number, min: 0, max: 5, step: 0.1 },
// { text: 'Minimum Age', value: 'min_age', sortable: false, type: Number, min: 4, max: 18, step: 1 },
// { text: 'Min Players', value: 'min_players', sortable: false, type: Number, min: 1, max: 10, step: 1 },
// { text: 'Max Players', value: 'max_players', sortable: false, type: Number, min: 1, max: 20, step: 1 },
// { text: 'Min Play Time', value: 'min_play_time', sortable: false, type: Number, min: 1, max: 3 * 60, step: 15 },
// { text: 'Max Play Time', value: 'max_play_time', sortable: false, type: Number, min: 1, max: 12 * 60, step: 15 }

class StringField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: String
    }
  }
}

class ChoicesField extends StringField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      class: 'ChoicesField',
      component: 'Choices'
    }
  }

  get $requiredArguments () {
    return [
      'label', 'prop', 'choices'
    ]
  }

  $init () {
    this.filters = Object.entries(this.choices).map(([value, text]) => ({ text, value }))
  }
}

const types = [
  Field,
  StringField,
  ChoicesField
]

export default new Registry(types)
