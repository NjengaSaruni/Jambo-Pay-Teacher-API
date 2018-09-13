from rest_framework import serializers

from common.models import Comment, Like
from common.serializers import AbstractFieldsMixin, CommentSerializer, CommentInlineSerializer, LikeSerializer
from divisions.serializers import ClassLevelInlineSerializer, ClassRoomInlineSerializer, \
    InstitutionSubjectInlineSerializer, ClassInlineSerializer, StudentInlineSerializer
from exams.models import ExamPaper, ClassExamResult, Grade, StudentPerformance, ClassPaperPerformance, Exam
from users.serializers import LikeInlineSerializer


class ExamSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    def create_results_folder(self, exam):
        for level in exam.class_levels.all():
            for cls in level.classes.all():
                if not ClassExamResult.objects.filter(_class=cls, exam=exam).exists():
                    ClassExamResult.objects.create(created_by=exam.created_by, exam=exam, _class=cls)

    def create(self, validated_data):
        exam = super(ExamSerializer, self).create(validated_data)

        self.create_results_folder(exam)

        return exam

    def update(self, exam, validated_data):
        exam = super(ExamSerializer, self).update(exam, validated_data)

        self.create_results_folder(exam)

        return exam

    class Meta:
        model = Exam
        fields = '__all__'


class ExamInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class_levels = ClassLevelInlineSerializer(read_only=True, many=True)

    class Meta:
        model = Exam
        fields = ('id',  'created_at', 'created_by','name', 'class_levels', 'start_date', 'end_date')

class ExamPaperInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    exam = ExamInlineSerializer(read_only=True)
    subject = InstitutionSubjectInlineSerializer(read_only=True)
    location = ClassRoomInlineSerializer(read_only=True)
    classes = ClassInlineSerializer(many=True, read_only=True)

    class Meta:
        model = ExamPaper
        fields = ('id', 'created_by','url','exam','subject','start','duration','total_mark','location', 'classes')


class ExamListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    class_levels = ClassLevelInlineSerializer(read_only=True, many=True)
    papers = ExamPaperInlineSerializer(read_only=True, many=True)

    class Meta:
        model = Exam
        fields = ('id', 'created_by','name', 'class_levels','start_date', 'end_date', 'done', 'papers', 'number')


class ExamPaperSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    def update(self, paper, validated_data):
        paper = super(ExamPaperSerializer, self).update(paper, validated_data)

        for cls in paper.classes.all():
            exam_folder, _ = ClassExamResult.objects.get_or_create(exam=paper.exam, _class=cls)
            class_exam_paper_performance = None

            if not ClassPaperPerformance.objects.filter(paper=paper, class_result = exam_folder).exists():
                class_exam_paper_performance = ClassPaperPerformance.objects.create(
                    paper=paper, class_result = exam_folder, created_by=paper.created_by
                )

            for student in cls.students.all():
                if not StudentPerformance.objects.filter(
                        student=student, class_performance=class_exam_paper_performance
                ).exists():
                    student_paper_performance = StudentPerformance(
                        student=student, class_performance=class_exam_paper_performance, created_by=paper.created_by
                    )

                    student_paper_performance.save()

            class_exam_paper_performance.save()

        return paper


    class Meta:
        model = ExamPaper
        fields = '__all__'


class ExamPaperListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    exam = ExamInlineSerializer(read_only=True)
    subject = InstitutionSubjectInlineSerializer(read_only=True)
    location = ClassRoomInlineSerializer(read_only=True)
    classes = ClassInlineSerializer(many=True, read_only=True)

    class Meta:
        model = ExamPaper
        fields = ('id', 'created_by','url','exam','subject','start','duration','total_mark','location', 'end', 'classes')


class GradeInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('id', 'created_by', 'name')


class GradeSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = '__all__'

class StudentClassPaperPerformanceInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    '''
    Used in StudentPaperPerformanceListSerializer to prevent redundancy
    '''
    _class = ClassInlineSerializer(read_only=True)
    paper = ExamPaperInlineSerializer(read_only=True)

    class Meta:
        model = ClassPaperPerformance
        fields = ('id', 'created_by', 'paper', 'grade', '_class')


class StudentPaperPerformanceListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    student = StudentInlineSerializer(read_only=True)
    grade = GradeInlineSerializer(read_only=True)
    class_performance = StudentClassPaperPerformanceInlineSerializer(read_only=True)
    comments = CommentInlineSerializer(read_only=True, many=True)
    likes = LikeInlineSerializer(read_only=True, many=True)
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = StudentPerformance
        fields = ('id', 'mark', 'rank','grade',
                  'class_performance','student', 'created_at', 'comments',
                  'likes', 'like_count')


class StudentPaperPerformanceSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    @staticmethod
    def add(exam_result, comments, likes):
        """

        :type exam_result: StudentPerformance
        """
        for comment in comments:
            comment = Comment.objects.create(**comment)
            exam_result.comments.add(comment)

        for like in likes:
            like = Like.objects.create(**like)
            exam_result.likes.add(like)

        exam_result.save()

        return exam_result

    def update(self, exam_result, validated_data):
        """

        :type exam_result: StudentPerformance
        """
        comments = validated_data.pop('comments', [])
        likes = validated_data.pop('likes', [])

        exam_result = super(StudentPaperPerformanceSerializer, self).update(exam_result, validated_data)

        return StudentPaperPerformanceSerializer.add(exam_result, comments, likes)

    class Meta:
        model = StudentPerformance
        fields = '__all__'

class StudentPaperPerformanceInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    student = StudentInlineSerializer(read_only=True)
    grade = GradeInlineSerializer(read_only=True)

    class Meta:
        model = StudentPerformance
        fields = ('id', 'created_by', 'student', 'grade', 'mark', 'rank')

class ClassPaperPerformanceListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    total = serializers.ReadOnlyField()
    mean = serializers.ReadOnlyField()
    grade = serializers.ReadOnlyField()
    paper = ExamPaperInlineSerializer(read_only=True)
    student_performances = StudentPaperPerformanceInlineSerializer(read_only=True, many=True)

    class Meta:
        model = ClassPaperPerformance
        fields = '__all__'

class ClassPaperPerformanceSerializer(AbstractFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = ClassPaperPerformance
        fields = '__all__'


class ClassPaperPerformanceInlineSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    _class = ClassInlineSerializer(read_only=True)
    paper = ExamPaperInlineSerializer(read_only=True)
    # student_performances = StudentPaperPerformanceInlineSerializer(read_only=True, many=True)
    mean = serializers.ReadOnlyField()

    class Meta:
        model = ClassPaperPerformance
        fields = ('id', 'created_by', 'paper', 'grade', 'mean','_class')

class ClassExamResultSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    @staticmethod
    def add_comments(exam_result, comments):
        for comment in comments:
            comment = Comment.objects.create(**comment)
            exam_result.comments.add(comment)

        exam_result.save()

        return exam_result

    def create(self, validated_data):
        comments = validated_data.pop('comments', [])
        exam_result = super(ClassExamResultSerializer,self).create(validated_data)

        return ClassExamResultSerializer.add_comments(exam_result, comments)

    def update(self, exam_result, validated_data):
        comments = validated_data.pop('comments', [])

        exam_result = super(ClassExamResultSerializer, self).update(exam_result, validated_data)

        return ClassExamResultSerializer.add_comments(exam_result, comments)

    class Meta:
        model = ClassExamResult
        fields = '__all__'

class ClassExamResultListSerializer(AbstractFieldsMixin, serializers.ModelSerializer):
    _class = ClassInlineSerializer(read_only=True)
    exam = ExamInlineSerializer(read_only=True)
    comments = CommentInlineSerializer(read_only=True, many=True)
    paper_performances = ClassPaperPerformanceInlineSerializer(read_only=True, many=True)
    total = serializers.ReadOnlyField()


    class Meta:
        model = ClassExamResult
        fields = ('id', 'created_by','comments', 'paper_performances','exam', '_class', 'total')