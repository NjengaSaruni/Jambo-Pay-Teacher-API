import django_filters

from common.filters import CommonFieldsFilterset
from messaging.models import PostComment


class PostCommentFilter(CommonFieldsFilterset):
    """
    Filters for the JoinRequest model
    """
    post = django_filters.CharFilter(name='post')

    class Meta(object):
        model = PostComment
        fields = [
            'post'
        ]
        order_by = ['-created_at', '-updated_at', 'active']
