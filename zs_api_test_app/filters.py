from django_filters import FilterSet
from django_filters import rest_framework as filters
from .models import *


class CountryFilter(FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    code = filters.CharFilter(field_name="code")

    class Meta:
        model = Country
        fields = ['name', 'code']


class StateFilter(FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = State
        fields = ['name']


class AddressFilter(FilterSet):
    house_no = filters.CharFilter(field_name="house_no", lookup_expr='icontains')
    road_no = filters.CharFilter(field_name="road_no", lookup_expr='icontains')

    class Meta:
        model = Address
        fields = ['house_no', 'road_no']
