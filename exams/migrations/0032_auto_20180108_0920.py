# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-08 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0021_studentcomment_notified'),
        ('exams', '0031_studentperformance_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentperformance',
            options={'ordering': ['student']},
        ),
        migrations.AlterUniqueTogether(
            name='studentperformance',
            unique_together=set([('student', 'class_performance')]),
        ),
    ]
