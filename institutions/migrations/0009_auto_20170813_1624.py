# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0008_auto_20170813_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='motto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
