"""
chooses which fields to be displayed for each of the classes
"""
import django_filters

from common.filters import CommonFieldsFilterset
from users.models import InstitutionJoinRequest, UserProfile


class JoinRequestFilter(CommonFieldsFilterset):
    """
    Filters for the JoinRequest model
    """
    type = django_filters.CharFilter(name='created_by__account_type__name')
    approved = django_filters.BooleanFilter(name='approved', lookup_expr='isnull', exclude=True)

    class Meta(object):
        model = InstitutionJoinRequest
        fields = [
            'institution', 'type', 'approved'
        ]
        order_by = ['-created_at', '-updated_at', 'active', 'deleted','approved']


class UserProfileFilter(CommonFieldsFilterset):
    """
    Filters for the JoinRequest model
    """
    created_by = django_filters.CharFilter(name='created_by')

    class Meta(object):
        model = UserProfile
        fields = [
            'created_by'
        ]
        order_by = ['-created_at', 'created_by' '-updated_at', 'active', 'deleted']