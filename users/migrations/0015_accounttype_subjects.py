# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-27 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_comment'),
        ('users', '0014_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounttype',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='common.Subject'),
        ),
    ]
