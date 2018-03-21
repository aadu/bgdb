// Game Model
import { Model } from '@vuex-orm/core'

export class Game extends Model {
  static entity = 'games'

  static fields () {
    return {
      id: this.attr(null),
      name: this.attr(''),
      description: this.attr(''),
      min_play_time: this.attr(null),
      max_play_time: this.attr(null),
      min_players: this.attr(null),
      max_players: this.attr(null),
      min_age: this.attr(null),
      max_age: this.attr(null)
    }
  }
}

export class Mechanic extends Model {
  static entity = 'mechanics'

  static fields () {
    return {
      id: this.attr(null),
      name: this.attr(''),
      description: this.attr('')
    }
  }
}
