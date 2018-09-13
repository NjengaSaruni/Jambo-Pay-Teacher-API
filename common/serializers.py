from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from common.models import Subject, Comment, Color, Like


def inline_creation(object, **inlined_data):
    pass

def pop_data(validated_data, *required_data):
    return {
               'user': validated_data.pop('user', []),
           }, validated_data

class AbstractFieldsMixin(object):
    """
    Injects the fields in the abstract base model as a model
    instance is being saved.
    """
    def __init__(self, *args, **kwargs):
        super(AbstractFieldsMixin, self).__init__(*args, **kwargs)

    def to_internal_value(self, data):
        """
        Mutate created_by during create
        :param data: The data as received in request
        :return: The data after ensuring missing fields cleaned
        """
        if self.context['request'].method == 'POST':
            if not 'created_by' in data or data['created_by'] is None:
                data['created_by'] = self.context['request'].user.id

        return super(AbstractFieldsMixin, self).to_internal_value(data)

    @transaction.atomic
    def create(self, validated_data):
        """`created` and `created_by` are only mutated if they are null"""
        if not validated_data.get('created_at', None):
            validated_data['created_at'] = timezone.now()


        validated_data['updated_at'] = timezone.now()
        validated_data['active'] = True

        if not validated_data.get('created_by', None):
            validated_data['created_by'] = self.context['request'].user

        try:
            object = self.Meta.model.objects.create(**validated_data)
            return object;
        except TypeError:
            validated_data.pop('created_by')
            return self.Meta.model.objects.create(**validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        # Make  sure the updated_at field is set to current time
        validated_data['updated_at'] = timezone.now()

        # Creator of object is immutable
        validated_data.pop('created_by', None)


        return super(AbstractFieldsMixin, self).update(instance, validated_data)


class SubjectSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    def create(self, validated_data):
        types = validated_data.pop('institution_types', [])

        subject =super(SubjectSerializer, self).create(validated_data)

        for type in types:
            subject.institution_types.add(type)
            subject.save()

        return subject

    class Meta:
        model = Subject
        fields = '__all__'

class SubjectInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name', 'description')


class CommentSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'title', 'replies','created_by', 'content')


class LikeSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'