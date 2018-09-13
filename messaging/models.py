# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from common.models import AbstractBase
from config import settings
from uploads.models import Image, File


class Notification(AbstractBase):
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255, null=True, blank=True)
    viewed = models.BooleanField(blank=True, default=False)
    sent = models.BooleanField(blank=True, default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):  # custom method for Notification
        return '{} - {} - {}'.format(self.created_by.institution.company, self.title, self.user.full_name)

    class Meta:  # add extra attributes (Metadata) to Notification
        app_label = 'messaging'


class Post(AbstractBase):
    text = models.TextField()
    images = models.ManyToManyField(Image, related_name='posts', blank=True)
    files = models.ManyToManyField(File, related_name='posts', blank=True)
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_posts')

    def get_like_count(self):
        return self.likers.count()

    likes = property(get_like_count)


    def get_comment_count(self):
        return self.comments.count()


    comment_count = property(get_comment_count)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.created_by.institution.name, self.created_by.full_name, self.text)

    class Meta:  # add extra attributes (Metadata) to Post
        app_label = 'messaging'
        ordering = ['-created_at']

class PostComment(AbstractBase):
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='comments')
    replies = models.ManyToManyField('self', related_name='comments', blank=True)
    likers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked_post_comments')

    def get_like_count(self):
        return self.likers.count()

    likes = property(get_like_count)


    def __unicode__(self):
        return '{} - {} - {}'.format(self.created_by.institution.name, self.created_by.full_name, self.text)


    class Meta:  # add extra attributes (Metadata) to PostComment
        app_label = 'messaging'

