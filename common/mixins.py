import operator
from django.db.models import Q
class GetQuerysetBaseMixin(object):
    def get_queryset(self, *args, **kwargs):
        self.queryset = super(GetQuerysetBaseMixin, self).get_queryset(*args, **kwargs)

        query = self.request.GET.get("q") or False
        # An icontains search using values in search fields specified in the calling view


        if query and hasattr(self, 'search_fields'):
            fields = [(field + '__icontains', query) for field in self.search_fields]

            q_list = [Q(x) for x in fields]

            self.queryset = self.queryset.filter(
                reduce(operator.or_, q_list)
            )

            self.queryset = self.queryset.distinct()

        return self.queryset

class GetQuerysetMixin(GetQuerysetBaseMixin):
    user = None

    def filter_by_institution(self):
        """
            Tries to get the institution to which a given object belongs
        """
        return self.queryset.filter(
            created_by__institution=self.request.user.institution
        ).exclude(
            created_by__institution=None
        )


    def get_queryset(self, *args, **kwargs):
        self.queryset = super(GetQuerysetMixin, self).get_queryset(*args, **kwargs)

        self.user = self.request.user

        self.queryset = self.filter_by_institution()

        return  self.queryset