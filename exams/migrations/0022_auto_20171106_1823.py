# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-06 18:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0021_auto_20171106_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classexampaperperformance',
            name='class_result',
        ),
        migrations.RemoveField(
            model_name='classexampaperperformance',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='classexampaperperformance',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='classexampaperperformance',
            name='paper',
        ),
        migrations.AlterUniqueTogether(
            name='studentpaperperformance',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='studentpaperperformance',
            name='class_performance',
        ),
        migrations.RemoveField(
            model_name='studentpaperperformance',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='studentpaperperformance',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='studentpaperperformance',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='studentpaperperformance',
            name='student',
        ),
        migrations.DeleteModel(
            name='ClassExamPaperPerformance',
        ),
        migrations.DeleteModel(
            name='StudentPaperPerformance',
        ),
    ]