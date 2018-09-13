# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-24 15:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0027_studentperformance_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classpaperperformance',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_performance', to='exams.ExamPaper'),
        ),
    ]
