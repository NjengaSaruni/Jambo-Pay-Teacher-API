from rest_framework import serializers

from common.serializers import AbstractFieldsMixin
from messaging.models import Post, PostComment
from uploads.serializers import FileInlineSerializer, ImageInlineSerializer
from users.serializers import UserInlineSerializer


class PostCommentSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = PostComment
        fields = '__all__'

class PostCommentListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    created_by = UserInlineSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = '__all__'

class PostCommentInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    created_by = UserInlineSerializer(read_only=True)

    class Meta:
        model = PostComment
        fields = ('id', 'text', 'created_by', 'likes')

class PostSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    def update(self, post, validated_data):
        likers = validated_data.pop('likers', None)

        post = super(PostSerializer, self).update(post, validated_data)

        if likers is not None:
            post.likers.add(likers[0])
            post.save()

        return post


    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    files = FileInlineSerializer(many=True, read_only=True)
    images = ImageInlineSerializer(many=True, read_only=True)
    created_by = UserInlineSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'created_at', 'likes', 'comment_count' ,'text' ,'files', 'images', 'comments', 'created_by')