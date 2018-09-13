# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-05 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_auto_20170903_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(blank=True, related_name='_comment_replies_+', to='common.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(default='Some title for the comment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
