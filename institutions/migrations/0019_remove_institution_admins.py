# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0018_auto_20170821_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institution',
            name='admins',
        ),
    ]
