import django_filters

from common.filters import CommonFieldsFilterset
from divisions.models import Class, StudentComment, Student


class ClassFilter(CommonFieldsFilterset):
    """
    Filters for the Class model
    """
    level = django_filters.CharFilter(name='level')

    class Meta(object):
        model = Class
        fields = [
            'level'
        ]
        order_by = ['-created_at', '-updated_at', 'active', 'deleted']


class StudentCommentFilter(CommonFieldsFilterset):

    student = django_filters.CharFilter(name='student')

    class Meta(object):
        model = StudentComment
        fields = [
            'student'
        ]
        order_by=['-created_at', '-updated_at']

class StudentFilter(CommonFieldsFilterset):
    user = django_filters.CharFilter(name='user')

    class Meta(object):
        model = Student
        fields = [
            'user'
        ]
        order_by = ['-created_at', '-updated_at']