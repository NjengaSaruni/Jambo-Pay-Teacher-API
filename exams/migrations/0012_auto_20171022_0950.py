# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-22 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0011_auto_20171022_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
