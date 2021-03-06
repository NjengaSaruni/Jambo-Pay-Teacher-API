# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 21:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0002_institution_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='image',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.Institution'),
        ),
        migrations.AddField(
            model_name='file',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='institution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.Institution'),
        ),
    ]
