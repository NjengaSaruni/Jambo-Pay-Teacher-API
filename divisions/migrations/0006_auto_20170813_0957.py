# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0005_auto_20170813_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='class_level',
            new_name='level',
        ),
    ]