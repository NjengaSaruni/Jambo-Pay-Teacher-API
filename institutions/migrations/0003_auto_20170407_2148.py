# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0002_institution_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
