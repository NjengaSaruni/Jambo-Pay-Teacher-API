from rest_framework import serializers

from common.serializers import AbstractFieldsMixin
from divisions.serializers import StudentInlineSerializer, InstitutionSubjectInlineSerializer, ClassInlineSerializer
from intelligence.models import StudentPrediction, ClassSubjectPrediction


class ClassSubjectPredictionSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ClassSubjectPrediction
        fields = '__all__'


class ClassSubjectPredictionListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    subject = InstitutionSubjectInlineSerializer(read_only=True)
    _class = ClassInlineSerializer(read_only=True)
    gradient = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model = ClassSubjectPrediction
        fields = ('id', 'created_at', 'subject', '_class', 'gradient')

class StudentPredictionSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentPrediction
        fields = '__all__'


class StudentPredictionListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    student = StudentInlineSerializer(read_only=True)


    class Meta:
        model = StudentPrediction
        fields = '__all__'

