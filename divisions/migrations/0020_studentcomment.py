# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-06 11:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('divisions', '0019_classroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentComment',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(default=False)),
                ('comment', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='divisions.Student')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
