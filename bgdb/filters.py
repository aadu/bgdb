import django_filters
from django.db.models import F


class CustomOrderingFilter(django_filters.OrderingFilter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_ordering_value(self, param):
        descending = param.startswith('-')
        param = param[1:] if descending else param
        field = F(self.param_map.get(param, param))
        return field.desc(nulls_last=True) if descending else field.asc(nulls_last=True)
