# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-11 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0016_auto_20170911_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='class_teacher_of',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='divisions.Class'),
        ),
    ]