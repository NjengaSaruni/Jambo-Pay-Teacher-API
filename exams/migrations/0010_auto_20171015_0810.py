# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20171012_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exampaper',
            name='start_time',
        ),
        migrations.AddField(
            model_name='exampaper',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
