# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 16:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('divisions', '0006_auto_20170813_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='divisions.Class'),
        ),
    ]