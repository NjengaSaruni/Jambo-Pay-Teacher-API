# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-03 14:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0008_auto_20170831_1936'),
        ('divisions', '0010_stream_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionSubject',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Subject')),
            ],
        ),
    ]
