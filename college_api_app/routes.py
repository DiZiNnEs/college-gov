from django.urls import path
from rest_framework.routers import DefaultRouter

from college_api_app.views import CollegeViewSet

router = DefaultRouter()

router.register(r'college', CollegeViewSet)
