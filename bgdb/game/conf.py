from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from appconf import AppConf
from model_utils import Choices


class GamesAppConf(AppConf):
    TYPES = Choices(
        ('game', _('game')),
        ('expansion', _('expansion')),
        ('accessory', _('accessory')),
        ('edition', _('edition')),
    )
    prefix = 'game'