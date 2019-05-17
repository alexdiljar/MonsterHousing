import django_filters
from Properties.models import Addresses

class PropertiesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    #class Meta:
       # model = Addresses
       # fields = ('street', 'house_no')
