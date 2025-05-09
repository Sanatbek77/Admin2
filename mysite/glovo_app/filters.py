from django_filters.rest_framework import FilterSet
from .models import Store


class StoreFilter(FilterSet):
    class Meta:
        model = Store
        fields = {
            'category': ['exact']
        }