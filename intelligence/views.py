from rest_framework import generics

from common.mixins import GetQuerysetMixin
from intelligence.filters import StudentPredictionFilter
from intelligence.models import StudentPrediction, ClassSubjectPrediction
from intelligence.serializers import StudentPredictionSerializer, StudentPredictionListSerializer, \
    ClassSubjectPredictionSerializer, ClassSubjectPredictionListSerializer


class StudentPredictionListView(GetQuerysetMixin, generics.ListAPIView):
    serializer_class = StudentPredictionSerializer
    queryset = StudentPrediction.objects.all()
    filter_class = StudentPredictionFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentPredictionListSerializer
        return StudentPredictionSerializer

class StudentPredictionDetailView(GetQuerysetMixin, generics.RetrieveDestroyAPIView):
    serializer_class = StudentPredictionSerializer
    queryset = StudentPrediction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentPredictionListSerializer
        return StudentPredictionSerializer


class ClassSubjectPredictionListView(GetQuerysetMixin, generics.ListAPIView):
    serializer_class = ClassSubjectPredictionSerializer
    queryset = ClassSubjectPrediction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassSubjectPredictionListSerializer
        return ClassSubjectPredictionSerializer


class ClassSubjectPredictionDetailView(GetQuerysetMixin, generics.RetrieveAPIView):
    serializer_class = ClassSubjectPredictionSerializer
    queryset = ClassSubjectPrediction.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassSubjectPredictionListSerializer
        return ClassSubjectPredictionSerializer