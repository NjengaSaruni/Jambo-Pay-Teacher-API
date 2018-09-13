# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps

from django.contrib import admin


for model in apps.get_app_config('uploads').models.values():
    admin.site.register(model)