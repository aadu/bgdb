import Registry from './registry'
import Field from './base'

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

class TextField extends StringField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: 'Text'
    }
  }
}

class PasswordField extends StringField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: 'password',
      readonly: true
    }
  }
}

class TimestampField extends StringField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      formatter: (v) => {
        if (v === undefined || v === null) {
          return ''
        }
        const date = new Date(v * 1000)
        return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`
      }
    }
  }
}

class DateField extends StringField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      formatter: (v) => {
        if (v === undefined || v === null) {
          return ''
        }
        const date = new Date(v)
        return `${date.toLocaleDateString()}`
      }
    }
  }
}

class DateTimeField extends StringField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      formatter: (v) => {
        if (v === undefined || v === null) {
          return ''
        }
        const date = new Date(v)
        return `${date.toLocaleDateString()} ${date.toLocaleTimeString()}`
      }
    }
  }
}

class ModelField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: Object,
      required: true,
      formatter: v => v ? v.name : undefined,
      multiple: false,
      disableLinks: false
    }
  }

  get $requiredArguments () {
    return [
      'label', 'prop', 'source'
    ]
  }

  $init () {
    if (this.multiple === true && this.disableLinks === true) {
      this.formatter = v => v ? v.map(o => o.name).join(', ') : v
    } else if (this.multiple === true) {
      this.formatter = v => v
      this.component = 'LinkMultiple'
    } else {
      this.component = 'Link'
    }
  }
}

class KeyValueField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      required: false,
      type: Object,
      default: {},
      component: 'KeyValue'
    }
  }
}

class JSONField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: 'JSON',
      component: 'JSON',
      default: {},
      filterable: false
    }
  }
}

class BooleanField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: Boolean,
      component: 'Boolean',
      default: false
    }
  }
}

class NumberField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      type: Number,
      min: 0,
      max: undefined,
      step: 1
    }
  }
}

class ArrayField extends Field {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      default: [],
      type: Array,
      filterable: false
    }
  }
}

class DateTimeRangeField extends ArrayField {
  get $defaults () {
    return {
      ...Object.getPrototypeOf(this).$defaults,
      formatter: (range) => {
        if (range === undefined || range === null) {
          return []
        } else {
          return range
        }
      }
    }
  }
}

const ID = new Field('id', {readonly: true, label: 'ID'})

const Name = new StringField('name', {
  required: true,
  sortable: true,
  minWidth: 250
})

const Description = new StringField('description')

const Project = new ModelField('project', {
  source: 'projects',
  required: true,
  sortable: true
})

const Labels = new KeyValueField('labels')

const Modified = new DateTimeField('modified', {
  sortable: true,
  readonly: true,
  width: 180
})

const Created = new DateTimeField('created', {
  sortable: true,
  readonly: true,
  width: 180
})

const types = [
  Field,
  StringField,
  ChoicesField,
  TextField,
  DateField,
  TimestampField,
  DateTimeField,
  NumberField,
  ModelField,
  KeyValueField,
  JSONField,
  ArrayField,
  BooleanField,
  PasswordField,
  DateTimeRangeField,
  {ID},
  {Name},
  {Description},
  {Project},
  {Labels},
  {Modified},
  {Created}
]

export default new Registry(types)
