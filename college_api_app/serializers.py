from rest_framework.serializers import ModelSerializer

from college_api_app.models import College


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = ('id', 'type', 'title', 'category', 'street', 'email', 'type', 'country', 'city', 'budget')
