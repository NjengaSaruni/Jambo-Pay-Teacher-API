from __future__ import unicode_literals

from django.db import models

# Create your models here.

from reversion import revisions as reversion

from common.models import AbstractBase


def unique_file_location(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.id, extension)
    return '/'.join(['Files', str(instance.created_at.date()), filename])


def unique_image_location(instance, filename):
    extension = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.id, extension)
    return '/'.join(['Image', str(instance.created_at.date()), filename])


@reversion.register
class File(AbstractBase):
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.FileField(upload_to=unique_file_location)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'uploads'


@reversion.register
class Image(AbstractBase):
    caption = models.CharField(max_length=255, null=True, blank=True)
    url = models.ImageField(upload_to=unique_image_location)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.caption or ''

    class Meta:
        app_label = 'uploads'