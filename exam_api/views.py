from rest_framework import viewsets
from . import models, serializers
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ExamView(viewsets.ModelViewSet):
    serializer_class = serializers.ExamSerializer

    def get_queryset(self):
        queryset = models.Exam.objects.all()
        return queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','years']


class YearView(viewsets.ModelViewSet):
    serializer_class = serializers.YearSerializer

    def get_queryset(self):
        queryset = models.Year.objects.all()
        return queryset

class MonthView(viewsets.ModelViewSet):
    serializer_class = serializers.MonthSerializer
    

    def get_queryset(self):
        queryset = models.Month.objects.all()
        return queryset



class SubjectView(viewsets.ModelViewSet):
    serializer_class = serializers.SubjectSerializer

    def get_queryset(self):
        queryset = models.Subject.objects.all()
        return queryset

class QuestionView(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        queryset = models.Question.objects.all()
        return queryset
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','exam','month','year', 'subject']

class AnswerView(viewsets.ModelViewSet):
    serializer_class = serializers.AnswerSerializer

    def get_queryset(self):
        queryset = models.Answer.objects.all()
        return queryset

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','exam','month','year', 'subject', 'question']