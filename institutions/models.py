from __future__ import unicode_literals

import uuid

from django.conf import settings
from django.db import models

class InstitutionType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    divisions_name = models.CharField(max_length=255, null=True, blank=True)
    levels = models.PositiveIntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'institutions'

class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True,default=uuid.uuid4, blank=True)
    motto = models.CharField(max_length=255, null=True,blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    physical_address = models.TextField(null=True, blank=True)
    postal_address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_institutions')
    type = models.ForeignKey(InstitutionType, null=True, blank=True)
    active = models.BooleanField(default=True, blank=True)

    def clean(self):
        if not self.domain:
            self.domain = self.name

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'institutions'
