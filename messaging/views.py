# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from common.mixins import GetQuerysetMixin
from messaging.filters import PostCommentFilter
from messaging.models import Post, PostComment
from messaging.serializers import PostSerializer, PostListSerializer, PostCommentSerializer, PostCommentListSerializer


class PostListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        return PostSerializer


class PostDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        return PostSerializer


class PostCommentListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    filter_class = PostCommentFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostCommentListSerializer
        return PostCommentSerializer


class PostCommentDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer