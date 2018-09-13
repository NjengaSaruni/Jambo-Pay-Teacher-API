from django.db import transaction
from rest_framework import serializers

from uploads.models import File
from uploads.serializers import FileSerializer, FileInlineSerializer
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    file = FileSerializer()

    @transaction.atomic
    def add_file(self, book, file):
        if file is not None:
            file = File.objects.create(**file)
            book.file = file
            book.save()
        return book

    @transaction.atomic
    def create(self, validated_data):
        file = validated_data.pop('file', None)
        book = super(BookSerializer, self).create(validated_data)

        return self.add_file(book, file)

    @transaction.atomic
    def update(self, book, validated_data):
        file = validated_data.pop('file', None)
        book = super(BookSerializer, self).update(book, validated_data)

        return self.add_file(book, file)

    class Meta:
        model = Book
        fields = '__all__'


class BookListSerializer(serializers.ModelSerializer):
    file = FileInlineSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
