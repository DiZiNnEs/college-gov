from django_filters import rest_framework as dj_filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets
from rest_framework.fields import CharField
from rest_framework import filters

from college_api_app.models import College
from college_api_app.serializers import CollegeSerializer


class CustomCategoryFilterSet(dj_filters.FilterSet):
    category = dj_filters.CharFilter(field_name='category__name')

    class Meta:
        model = College
        fields = ('id', 'type', 'title', 'category', 'street', 'email', 'type', 'country', 'city', 'budget')


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = CustomCategoryFilterSet
    filter_fields = ('category__name', 'type',)
    search_fields = ('title', 'country__name', 'city__name',)
    ordering_fields = ('title',)
