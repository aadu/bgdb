from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import get_language_info
from appconf import AppConf

from .languages import LANGUAGES


class GamesAppConf(AppConf):
    LANGUAGES = LANGUAGES

    prefix = 'game'