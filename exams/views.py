# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from common.mixins import GetQuerysetMixin
from exams.filters import ClassExamPaperPerformanceFilter, ClassExamResultFilter, StudentPaperPerformanceFilter
from exams.models import Exam, ExamPaper, ClassExamResult, StudentPerformance, ClassPaperPerformance, Grade
from exams.serializers import ExamPaperSerializer, ExamPaperListSerializer, ExamSerializer, ExamListSerializer, \
    ClassExamResultSerializer, ClassExamResultListSerializer, StudentPaperPerformanceSerializer, \
    StudentPaperPerformanceListSerializer, ClassPaperPerformanceSerializer, ClassPaperPerformanceListSerializer, \
    GradeSerializer
from users.models import User


class ExamListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    search_fields = (
        'name',
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamListSerializer
        return ExamSerializer

class ExamDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamListSerializer
        return ExamSerializer

class ExamPaperListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ExamPaperSerializer
    queryset = ExamPaper.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamPaperListSerializer
        return ExamPaperSerializer

class ExamPaperDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExamPaperSerializer
    queryset = ExamPaper.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ExamPaperListSerializer
        return ExamPaperSerializer

class ClassExamResultListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ClassExamResultSerializer
    queryset = ClassExamResult.objects.all()
    filter_class = ClassExamResultFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassExamResultListSerializer
        return ClassExamResultSerializer

class ClassExamResultDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassExamResultSerializer
    queryset = ClassExamResult.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassExamResultListSerializer
        return ClassExamResultSerializer


class StudentPaperPerformanceDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentPaperPerformanceSerializer
    queryset = StudentPerformance.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentPaperPerformanceListSerializer
        return StudentPaperPerformanceSerializer



class StudentPaperPerformanceListView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = StudentPaperPerformanceSerializer
    queryset = StudentPerformance.objects.all()
    filter_class = StudentPaperPerformanceFilter
    
    def get_queryset(self, *args, **kwargs):
        self.queryset = super(StudentPaperPerformanceListView, self).get_queryset()

        user = User.objects.get(id=self.request.user.id)

        if user.account_type.name == 'Parent':
            self.queryset.filter(student__in=user.parent.students.all())

        return self.queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentPaperPerformanceListSerializer
        return StudentPaperPerformanceSerializer


class ClassPaperPerformanceListView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ClassPaperPerformanceSerializer
    queryset = ClassPaperPerformance.objects.all()
    filter_class = ClassExamPaperPerformanceFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassPaperPerformanceListSerializer
        return ClassPaperPerformanceSerializer

class ClassPaperPerformanceDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassPaperPerformanceSerializer
    queryset = ClassPaperPerformance.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassPaperPerformanceListSerializer
        return ClassPaperPerformanceSerializer

class GradeListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()

class GradeDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GradeSerializer
    queryset = Grade.objects.all()