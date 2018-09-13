from __future__ import unicode_literals

import uuid

from django.utils import timezone
from django.conf import settings
from django.db import models

from institutions.models import InstitutionType

def get_unique_number(self):
    try:
        latest_object = type(self).objects.filter(institution=self.created_by.institution).latest('created_at')
        number = latest_object.number
        if number[:6] == timezone.now().date().strftime("%Y%m"):
            return number[:6] + format(int(number[-4:], 16) + 1, 'X').zfill(4)
        return str(timezone.now().date().strftime("%Y%m")) + '0000'

    except:
        return str(timezone.now().date().strftime("%Y%m")) + '0000'

class CustomDefaultManager(models.Manager):
    """
        Override default manager to never retrieve deleted objects
    """
    def get_queryset(self):
        return super(CustomDefaultManager, self).get_queryset().filter(
            deleted=False)

class AbstractBareBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True, blank=True)
    deleted = models.BooleanField(
        default=False,
        help_text="Deletes should deactivate not do actual deletes")

    objects = CustomDefaultManager()
    everything = models.Manager()

    def delete(self, *args, **kwargs):
        # Mark the field model deleted
        self.deleted = True
        self.save()

    class Meta(object):
        ordering = ('-updated_at', '-created_at',)
        abstract = True


class AbstractBase(AbstractBareBase):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False, blank=True)


    class Meta(object):
        ordering = ('-updated_at', '-created_at',)
        abstract = True

class Subject(AbstractBareBase):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    institution_types = models.ManyToManyField(InstitutionType, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'common'


class Like(AbstractBase):

    def __unicode__(self):
        return self.created_by.full_name


    class Meta:
        app_label = 'common'

class Comment(AbstractBase):
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    replies = models.ManyToManyField('self', blank=True ,related_name='parent')

    def __unicode__(self):
        return '{} - {} - {}'.format(self.created_by.institution.name, self.created_by.username, self.title)

    class Meta:
        app_label = 'common'


class Person(AbstractBase):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True, null=True, blank=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (
            (self.first_name or ''), (self.middle_name or ''), (self.last_name or ''))
        return full_name.strip()

    full_name = property(get_full_name)

    class Meta:
        app_label = 'common'


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hex = models.CharField(max_length=255)

    class Meta:
        app_label = 'common'