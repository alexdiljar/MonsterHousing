import django_filters


class PropertiesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
