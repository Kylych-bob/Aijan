from django.urls import path
from .views import ListApiCourse, DetailCourses, NewCourse

urlpatterns = [
    path('<int:pk>/', DetailCourses.as_view()),
    path('', ListApiCourse.as_view()),
    path('', NewCourse.as_view())
]