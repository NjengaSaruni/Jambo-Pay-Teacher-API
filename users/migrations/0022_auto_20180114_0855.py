# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-14 08:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_userprofile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-created_at']},
        ),
    ]
