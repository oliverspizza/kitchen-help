import django_filters
from accounts.models import Avaliablity


class AvaliablityFilter(django_filters.FilterSet):
    available = django_filters.CharFilter(field_name='not_available',help_text='filter by date (yyyy-mm-dd).')
    #date = django_filters.DateField()
    class Mets:
        model = Avaliablity
        fields = ['person', 'not_available']
