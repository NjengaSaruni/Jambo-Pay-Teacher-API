# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-06 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_like'),
        ('exams', '0030_auto_20180105_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentperformance',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='student_performances', to='common.Like'),
        ),
    ]
