# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-06 09:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_post_postcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]