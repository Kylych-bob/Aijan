from django.shortcuts import render

from rest_framework import generics
from .models import Course, Languages, Details

from.serializers import DetailsSerializer, DetailsPrLangSerializer, NewCourseSerializer


class ListApiCourse(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = DetailsSerializer


class DetailCourses(generics.RetrieveAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsPrLangSerializer


class NewCourse(generics.RetrieveAPIView):
    queryset = Languages.objects.all()
    serializer_class = NewCourseSerializer


