import django_filters

from common.filters import CommonFieldsFilterset
from exams.models import ClassPaperPerformance, ClassExamResult, StudentPerformance


class ClassExamPaperPerformanceFilter(CommonFieldsFilterset):
    """
    Filters for the ClassExamPaperPerformance model
    """
    paper = django_filters.CharFilter(name='paper')
    _class = django_filters.CharFilter(name='_class')

    class Meta(object):
        model = ClassPaperPerformance
        fields = [

            'paper', '_class'
        ]
        order_by = ['-created_at', '-updated_at', 'active', 'deleted']


class StudentPaperPerformanceFilter(CommonFieldsFilterset):
    """
    Filters for the ClassExamPaperPerformance model
    """
    class_performance = django_filters.CharFilter(name='class_performance')
    student = django_filters.CharFilter(name='student')
    exam = django_filters.CharFilter(
        name='class_performance__paper__exam')

    class Meta(object):
        model = StudentPerformance
        fields = [
            'class_performance', 'student', 'exam'
        ]
        order_by = ['student__name', '-created_at', '-updated_at', 'active', 'deleted']

class ClassExamResultFilter(CommonFieldsFilterset):
    """
    Filters for the ClassExamResult model
    """
    exam = django_filters.CharFilter(name='exam')
    _class = django_filters.CharFilter(name='_class')
    student = django_filters.CharFilter(name='student')

    class Meta(object):
        model = ClassExamResult
        fields = [
            'exam', '_class'
        ]
        order_by = ['-created_at', '-updated_at', 'active', 'deleted']