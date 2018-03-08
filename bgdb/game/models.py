from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _

from .conf import settings


class EntityModel(models.Model):
    name = models.CharField(_("name"), max_length=255, db_index=True)
    description = models.TextField(_("description"), blank=True, default='', db_index=True)
    slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-modified',)
        get_latest_by = 'modified'
        indexes = [
            models.Index(fields=['id', 'name']),
            models.Index(fields=['-created']),
            models.Index(fields=['-modified']),
        ]


class Game(EntityModel):
    # name = models.CharField(_("name"), max_length=255, db_index=True)
    # description = models.TextField(_("description"), blank=True, default='', db_index=True)
    # slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    # created = models.DateTimeField(_("created"), auto_now_add=True)
    # modified = models.DateTimeField(_("modified"), auto_now=True)
    year_published = models.PositiveIntegerField(_('year published'), blank=True, null=True)
    min_players = models.PositiveIntegerField(_('min players'), blank=True, null=True)
    max_players = models.PositiveIntegerField(_('max players'), blank=True, null=True)
    play_time = models.PositiveIntegerField(_('play time'), blank=True, null=True)
    min_play_time = models.PositiveIntegerField(_('min play time'), blank=True, null=True)
    max_play_time = models.PositiveIntegerField(_('max play time'), blank=True, null=True)
    min_age = models.PositiveIntegerField(_('min age'), blank=True, null=True)
    max_age = models.PositiveIntegerField(_('max age'), blank=True, null=True)

    class Meta(EntityModel.Meta):
        default_related_name = 'games'
        db_table = 'games'


class Type(EntityModel):
    # name = models.CharField(_("name"), max_length=255, db_index=True)
    # description = models.TextField(_("description"), blank=True, default='', db_index=True)
    # slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    # created = models.DateTimeField(_("created"), auto_now_add=True)
    # modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta(EntityModel.Meta):
        default_related_name = 'type'
        db_table = 'game_types'




# type (game, expansion, accessory, edition)
# domain
# category
# family
# mechanisms
