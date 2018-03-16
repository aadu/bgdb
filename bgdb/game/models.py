from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _

from .conf import settings

from bgdb.mixins import EntityModel


class Game(EntityModel):
    # name = models.CharField(_("name"), max_length=255, db_index=True)
    # description = models.TextField(_("description"), blank=True, default='', db_index=True)
    # slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    # created = models.DateTimeField(_("created"), auto_now_add=True)
    # modified = models.DateTimeField(_("modified"), auto_now=True)
    # url = models.URLField(_('url'), blank=True, default='')
    type = models.CharField(max_length=24, choices=settings.GAME_TYPES, default=settings.GAME_TYPES.game, blank=True)
    year_published = models.PositiveIntegerField(_('year published'), blank=True, null=True)
    min_players = models.PositiveIntegerField(_('min players'), blank=True, null=True)
    max_players = models.PositiveIntegerField(_('max players'), blank=True, null=True)
    play_time = models.PositiveIntegerField(_('play time'), blank=True, null=True)
    min_play_time = models.PositiveIntegerField(_('min play time'), blank=True, null=True)
    max_play_time = models.PositiveIntegerField(_('max play time'), blank=True, null=True)
    min_age = models.PositiveIntegerField(_('min age'), blank=True, null=True)
    max_age = models.PositiveIntegerField(_('max age'), blank=True, null=True)
    categories = models.ManyToManyField('game.Category', blank=True, verbose_name=_('categories'))
    subcategories = models.ManyToManyField('game.SubCategory', blank=True, verbose_name=_('subcategories'))
    mechanisms = models.ManyToManyField('game.Mechanism', blank=True, verbose_name=_('mechanisms'))
    reimplements = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='reimplemented_by', verbose_name=_('reimplements'))
    parent = models.ForeignKey('self', verbose_name=_('game'), on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta(EntityModel.Meta):
        default_related_name = 'games'
        db_table = 'games'


class Category(EntityModel):
    # name = models.CharField(_("name"), max_length=255, db_index=True)
    # description = models.TextField(_("description"), blank=True, default='', db_index=True)
    # slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    # created = models.DateTimeField(_("created"), auto_now_add=True)
    # modified = models.DateTimeField(_("modified"), auto_now=True)
    # url = models.URLField(_('url'), blank=True, default='')

    class Meta(EntityModel.Meta):
        default_related_name = 'categories'
        db_table = 'game_categories'


class Subcategory(EntityModel):
    # name = models.CharField(_("name"), max_length=255, db_index=True)
    # description = models.TextField(_("description"), blank=True, default='', db_index=True)
    # slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    # created = models.DateTimeField(_("created"), auto_now_add=True)
    # modified = models.DateTimeField(_("modified"), auto_now=True)
    # url = models.URLField(_('url'), blank=True, default='')

    class Meta(EntityModel.Meta):
        default_related_name = 'subcategories'
        db_table = 'game_subcategories'


class Mechanism(EntityModel):
    # name = models.CharField(_("name"), max_length=255, db_index=True)
    # description = models.TextField(_("description"), blank=True, default='', db_index=True)
    # slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    # created = models.DateTimeField(_("created"), auto_now_add=True)
    # modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta(EntityModel.Meta):
        default_related_name = 'mechanisms'
        db_table = 'game_mechanisms'
