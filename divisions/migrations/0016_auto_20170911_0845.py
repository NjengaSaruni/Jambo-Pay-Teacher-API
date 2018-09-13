# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-11 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0015_auto_20170910_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='class_teacher',
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_teacher_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='divisions.Class'),
        ),
    ]