import django_filters
from todo.models import PrepWork

class PrepWorkFilter(django_filters.FilterSet):
    item = django_filters.CharFilter(field_name='day_of_week',lookup_expr ='icontains')

    class Mets:
        model = PrepWork
        fields = ['item,''day_of_week']
