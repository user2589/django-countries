# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

import caching.base

class Country (caching.base.CachingMixin, models.Model):
    code            = models.CharField(max_length=2, primary_key=True, help_text=_('ISO 3166 country code'))
    name            = models.CharField(max_length=50, db_index=True)
    visible         = models.BooleanField(default=True, db_index=True)

    objects = caching.base.CachingManager()

    class Meta:
        db_table = 'countries'
        ordering = ('name',)
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __unicode__(self):
        return _(self.name)
