# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0003_auto_20170709_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='year',
            field=models.PositiveIntegerField(default=2017),
        ),
    ]
