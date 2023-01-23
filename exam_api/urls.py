from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'exams', views.ExamView, basename='exam')
router.register(r'years', views.YearView, basename='year')
router.register(r'months', views.MonthView, basename='month')
router.register(r'subjects', views.SubjectView, basename='subject')
router.register(r'questions', views.QuestionView, basename='question')
router.register(r'answers', views.AnswerView, basename='answer')

urlpatterns = [
  path('', include(router.urls))
  ]