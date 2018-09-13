from rest_framework import generics

from common.mixins import GetQuerysetMixin
from divisions.filters import ClassFilter, StudentCommentFilter, StudentFilter
from divisions.models import Student, Stream, ClassLevel, Class, Parent, Teacher, InstitutionSubject, ClassRoom, \
    StudentComment
from divisions.serializers import StudentSerializer, StudentListSerializer, StreamSerializer, ClassLevelSerializer, \
    ClassSerializer, ClassListSerializer, ParentSerializer, ParentListSerializer, TeacherSerializer, \
    TeacherListSerializer, StreamListSerializer, InstitutionSubjectSerializer, InstitutionSubjectListSerializer, \
    ClassRoomSerializer, ClassRoomListSerializer, ClassDetailSerializer, StudentCommentSerializer, \
    StudentCommentListSerializer
from users.models import User


class StreamListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = StreamSerializer
    queryset = Stream.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StreamListSerializer
        return StreamSerializer

class StreamDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StreamSerializer
    queryset = Stream.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StreamListSerializer
        return StreamSerializer


class ClassLevelListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ClassLevelSerializer
    queryset = ClassLevel.objects.all()


class ClassLevelDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassLevelSerializer
    queryset = ClassLevel.objects.all()


class ClassListCreateView(generics.ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()
    filter_class = ClassFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassListSerializer
        return ClassSerializer


class ClassDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassDetailSerializer
        return ClassSerializer


class StudentListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    search_fields = (
        'user__first_name', 'user__first_name', 'user__username',
        'user__last_name', 'registration_number', 'current_class__name'
    )
    filter_class = StudentFilter

    def get_queryset(self, *args, **kwargs):
        self.queryset = super(StudentListCreateView, self).get_queryset(*args, **kwargs)

        user = User.objects.get(id=self.request.user.id)

        if user.account_type.name == 'Parent':
            self.queryset = self.queryset.filter(parent=user.parent)

        return self.queryset

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentListSerializer
        return StudentSerializer


class StudentDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentListSerializer
        return StudentSerializer

class TeacherListCreateView(generics.ListCreateAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    search_fields = (
        'user__first_name', 'user__first_name', 'user__username', 'user__last_name', 'subjects__name'
    )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TeacherListSerializer
        return TeacherSerializer


class TeacherDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TeacherListSerializer
        return TeacherSerializer

class ParentListCreateView(GetQuerysetMixin,generics.ListCreateAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

    search_fields = (
        'user__first_name', 'user__first_name', 'user__username', 'user__last_name'
    )

    def get_queryset(self, *args, **kwargs):
        self.queryset = super(ParentListCreateView, self).get_queryset(*args, **kwargs)

        if self.request.user.account_type.name == 'Student':
            self.queryset = self.queryset.filter(id=self.request.user.student.parent.id)

        return self.queryset


    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParentListSerializer
        return ParentSerializer


class ParentDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ParentListSerializer
        return ParentSerializer

class InstitutionSubjectListCreateView(GetQuerysetMixin,generics.ListCreateAPIView):
    serializer_class = InstitutionSubjectSerializer
    queryset = InstitutionSubject.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InstitutionSubjectListSerializer
        return InstitutionSubjectSerializer


class InstitutionSubjectDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstitutionSubjectSerializer
    queryset = InstitutionSubject.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InstitutionSubjectListSerializer
        return InstitutionSubjectSerializer

class ClassRoomListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassRoomListSerializer
        return ClassRoomSerializer

class ClassRoomDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClassRoomListSerializer
        return ClassRoomSerializer

class StudentCommentListCreateView(GetQuerysetMixin, generics.ListCreateAPIView):
    serializer_class = StudentCommentSerializer
    queryset = StudentComment.objects.all()
    filter_class = StudentCommentFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentCommentListSerializer
        return StudentCommentSerializer


class StudentCommentDetailView(GetQuerysetMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentCommentSerializer
    queryset = StudentComment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return StudentCommentListSerializer
        return StudentCommentSerializer