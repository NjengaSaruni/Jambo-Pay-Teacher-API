# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-14 08:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0003_auto_20170709_0953'),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('files', models.ManyToManyField(blank=True, related_name='posts', to='uploads.File')),
                ('images', models.ManyToManyField(blank=True, related_name='posts', to='uploads.Image')),
                ('likers', models.ManyToManyField(blank=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False, help_text='Deletes should deactivate not do actual deletes')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('public', models.BooleanField(default=False)),
                ('text', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('likers', models.ManyToManyField(blank=True, related_name='liked_post_comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='messaging.Post')),
                ('replies', models.ManyToManyField(blank=True, related_name='_postcomment_replies_+', to='messaging.PostComment')),
            ],
        ),
    ]