# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-09 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0033_studentprediction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprediction',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='studentprediction',
            name='student',
        ),
        migrations.DeleteModel(
            name='StudentPrediction',
        ),
    ]