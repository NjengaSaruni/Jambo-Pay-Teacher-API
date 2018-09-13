from rest_framework import serializers

from common.serializers import AbstractFieldsMixin
from uploads.models import File, Image


class FileSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'created_by','title', 'url']


class ImageSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImageInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'created_by','caption', 'url']