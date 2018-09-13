import django_filters

from common.filters import CommonFieldsFilterset
from intelligence.models import StudentPrediction


class StudentPredictionFilter(CommonFieldsFilterset):
    """
    Filters for the StudentPrediction model
    """
    student = django_filters.CharFilter(name='student')
    subject = django_filters.CharFilter(name='subject')
    _class = django_filters.CharFilter(name='_class')

    class Meta(object):
        model = StudentPrediction
        fields = [
            'student', 'subject', '_class'
        ]
        order_by = ['student', '-created_at', '-updated_at', 'active', 'deleted']
