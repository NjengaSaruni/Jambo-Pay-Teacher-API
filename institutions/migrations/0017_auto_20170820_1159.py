# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 11:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0016_auto_20170820_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='phone_number',
            new_name='mobile',
        ),
    ]
