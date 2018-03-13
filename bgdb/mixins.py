from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _


class EntityModel(models.Model):
    name = models.CharField(_("name"), max_length=255, db_index=True)
    description = models.TextField(_("description"), blank=True, default='', db_index=True)
    slug = AutoSlugField(_("slug"), populate_from=['name'], db_index=True)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)
    url = models.URLField(_('url'), blank=True, default='')

    class Meta:
        abstract = True
        ordering = ('name',)
        get_latest_by = 'modified'
        indexes = [
            models.Index(fields=['id', 'name']),
            models.Index(fields=['-created']),
            models.Index(fields=['-modified']),
        ]