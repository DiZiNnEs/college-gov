from rest_framework import serializers

from college_api_app.models import College


class CollegeSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    country = serializers.ReadOnlyField(source='country.name')
    city = serializers.StringRelatedField()

    class Meta:
        model = College
        fields = ('id', 'type', 'title', 'category', 'street', 'email', 'type', 'country', 'city', 'budget')
