from rest_framework import viewsets

from college_api_app.models import College
from college_api_app.serializers import CollegeSerializer


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
