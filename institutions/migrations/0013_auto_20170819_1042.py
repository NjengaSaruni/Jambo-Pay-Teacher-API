# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 10:42
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0012_auto_20170819_1042'),
    ]

    operations = [
    ]
    migrations.AlterField(
        model_name='institution',
        name='domain',
        field=models.CharField(blank=True, default=uuid.uuid4, max_length=255, unique=True),
    ),
