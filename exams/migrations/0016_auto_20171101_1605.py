# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-01 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0015_exampaper_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exampaper',
            old_name='_classes',
            new_name='classes',
        ),
        migrations.AlterField(
            model_name='exampaper',
            name='start',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
