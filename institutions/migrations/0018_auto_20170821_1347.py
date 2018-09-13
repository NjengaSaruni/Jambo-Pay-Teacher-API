# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import uploads.models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0017_auto_20170820_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=uploads.models.unique_image_location),
        ),
    ]
