# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0004_auto_20170709_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institutionitem',
            name='object_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
