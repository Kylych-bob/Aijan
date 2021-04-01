from rest_framework import serializers
from .models import Course, Details


class DetailsSerializer(serializers.ModelSerializer):
    totally = serializers.SerializerMethodField()

    class Meta:
        model = Details
        fields = ['id', 'title', 'pr_languages', 'totally']


class DetailsPrLangSerializer(serializers.ModelSerializer):
    courses = DetailsSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'address', 'courses', 'totally']


class NewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ['id', 'title', 'pr_language', 'duration', 'price_per_month', 'totally']
