# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0004_class_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
