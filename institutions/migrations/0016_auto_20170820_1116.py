# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 11:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0015_institution_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin_of', to=settings.AUTH_USER_MODEL),
        ),
    ]
