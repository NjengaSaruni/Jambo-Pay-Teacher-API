from django.forms import model_to_dict
from rest_framework import serializers

from common.serializers import AbstractFieldsMixin, SubjectInlineSerializer, ColorSerializer
from divisions.models import Student, Class, ClassLevel, Stream, Teacher, Parent, InstitutionSubject, ClassRoom, \
    StudentComment
from users.models import User, AccountType
from users.serializers import UserInlineSerializer, UserSerializer


def create_user(validated_data, type):
    user = validated_data.pop('user', None)
    user['account_type'] = AccountType.objects.get(name=type)

    if user is not None:
        user = User.objects.create(**user)
        user.save()

    return user, validated_data

class ClassInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    # class_teacher = UserInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ('id', 'created_by','name','stream', 'level', 'class_teacher', 'created_at', 'updated_at')


class StudentInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)
    current_class = ClassInlineSerializer(read_only=True)

    class Meta:
        model = Student
        fields = ('id', 'created_by','user','current_class','created_by', 'parent')

class ParentInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)

    class Meta:
        model = Parent
        fields = ('id','created_by','user','token')

class InstitutionSubjectSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = InstitutionSubject
        fields = '__all__'

class InstitutionSubjectListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    subject = SubjectInlineSerializer(read_only=True)

    class Meta:
        model = InstitutionSubject
        fields = '__all__'

class InstitutionSubjectInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    subject = SubjectInlineSerializer(read_only=True)

    class Meta:
        model = InstitutionSubject
        fields = ['id', 'created_by', 'subject', 'name']


class StreamSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Stream
        fields = '__all__'

class StreamListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)

    class Meta:
        model = Stream
        fields = '__all__'


class StreamInlineSerializer(StreamSerializer):
    class Meta:
        model = Stream
        fields = ('id', 'created_by','name', 'color')

class ClassLevelSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = ClassLevel
        fields = '__all__'

class ClassLevelInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = ClassLevel
        fields = ('id','name','created_by','value')


class TeacherSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user, validated_data = create_user(validated_data, 'Teacher')
        teacher = super(TeacherSerializer, self).create(validated_data)

        user.institution = teacher.created_by.institution
        user.save()
        teacher.user = user
        teacher.save()

        return teacher

    def update(self, parent, validated_data):
        user, validated_data = create_user(validated_data, 'Parent')

        parent = super(ParentSerializer, self).update(validated_data)

        parent.user = user
        parent.save()

        return parent

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)
    classes = ClassInlineSerializer(read_only=True, many=True)
    subjects = InstitutionSubjectInlineSerializer(read_only=True, many=True)

    class Meta:
        model = Teacher
        fields = ('id','user','created_by','classes','subjects', 'created_at')


class TeacherInlineSerializer(TeacherListSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'created_by', 'classes', 'subjects')

class ClassSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    def create(self, validated_data):
        _class = super(ClassSerializer, self).create(validated_data)

        try:
            teacher = Teacher.objects.get(id=self.initial_data['class_teacher'])
            teacher.class_teacher_of = _class
            teacher.save()

        except (KeyError, Teacher.DoesNotExist):
            pass


        return _class

    class Meta:
        model = Class
        fields = '__all__'


class ClassListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    level = ClassLevelInlineSerializer(read_only=True)
    stream = StreamInlineSerializer(read_only=True)
    class_teacher = TeacherInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ('id', 'created_by','name','stream', 'level', 'class_teacher', 'created_at', 'updated_at')


class ClassDetailSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    level = ClassLevelInlineSerializer(read_only=True)
    stream = StreamInlineSerializer(read_only=True)
    class_teacher = TeacherInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)
    students = StudentInlineSerializer(many=True, read_only=True)

    class Meta:
        model = Class
        fields = ('id', 'created_by','name','stream', 'level', 'class_teacher', 'created_at', 'updated_at', 'students')


class StudentSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user, validated_data = create_user(validated_data, 'Student')
        student = super(StudentSerializer, self).create(validated_data)

        user.institution = student.created_by.institution
        user.save()
        student.user = user
        student.save()

        return student

    def update(self, student, validated_data):
        user, validated_data = create_user(validated_data, 'Student')

        student = super(StudentSerializer, self).update(validated_data)
        student.user = user
        student.save()

        return student


    class Meta:
        model = Student
        fields = '__all__'


class StudentListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)
    parent = ParentInlineSerializer(read_only=True)
    current_class = ClassInlineSerializer(read_only=True)

    def to_representation(self, instance):
        try:
            return super(StudentListSerializer, self).to_representation(instance)
        except AttributeError:
            return self.to_internal_value(model_to_dict(instance))

    class Meta:
        model = Student
        fields = '__all__'


class ParentSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserSerializer()

    def create(self, validated_data):
        user, validated_data = create_user(validated_data, 'Parent')
        students = self.initial_data.pop('students', [])

        parent = super(ParentSerializer, self).create(validated_data)

        for student in students:
            student = Student.objects.get(id=student)
            student.parent = parent
            student.save()

        user.institution = parent.created_by.institution
        user.save()
        parent.user = user
        parent.save()

        return parent

    def update(self, parent, validated_data):
        user, validated_data = create_user(validated_data, 'Parent')
        students = self.initial_data.pop('students', [])

        parent = super(ParentSerializer, self).update(validated_data)

        for student in students:
            student = Student.objects.get(id=student)
            student.parent = parent
            student.save()

        parent.user = user
        parent.save()

        return parent

    class Meta:
        model = Parent
        fields = '__all__'

class ParentListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    user = UserInlineSerializer(read_only=True)
    created_by = UserInlineSerializer(read_only=True)
    students = StudentInlineSerializer(read_only=True, many=True)

    class Meta:
        model = Parent
        fields = ('id','created_by','user','token', 'students')


class ClassRoomSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = ClassRoom
        fields = '__all__'

class ClassRoomListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    current_class = ClassInlineSerializer(read_only=True)

    class Meta:
        model = ClassRoom
        fields = ('id', 'created_at', 'updated_at', 'name', 'current_class', 'occupants')

class ClassRoomInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    current_class = ClassInlineSerializer(read_only=True)

    class Meta:
        model = ClassRoom
        fields = ('id', 'created_at', 'updated_at', 'name', 'current_class', 'occupants')



class StudentCommentSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = StudentComment
        fields = '__all__'


class StudentCommentListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    created_by = UserInlineSerializer(read_only=True)
    student = StudentInlineSerializer(read_only=True)

    class Meta:
        model = StudentComment
        fields = ('id', 'created_at', 'created_by', 'student', 'comment')