# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-27 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0020_auto_20170827_0835'),
        ('common', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='institution_types',
            field=models.ManyToManyField(blank=True, to='institutions.InstitutionType'),
        ),
    ]
