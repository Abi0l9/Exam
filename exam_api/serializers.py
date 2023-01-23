from rest_framework import serializers
from .models import Exam, Year, Month, Subject, Question, Answer

class ExamSerializer(serializers.ModelSerializer):
    years = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='year-detail')
    
    def get_years_count(self, obj):
        obj.name_count

    class Meta:
        fields = ['id', 'name', 'years']
        model = Exam

class YearSerializer(serializers.ModelSerializer):
    months = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='month-detail')

    class Meta:
        fields = ['id','months', 'year', 'exam']
        model = Year


class MonthSerializer(serializers.ModelSerializer):
    subjects = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='subject-detail')

    class Meta:
        fields = ['id', 'name', 'subjects', 'year', 'exam']
        model = Month


class SubjectSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='question-detail')

    class Meta:
        fields = ['id', 'name', 'month', 'year', 'exam', 'questions']
        model = Subject


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='answer-detail')

    class Meta:
        fields = ['id', 'question_text', 'subject', 'month', 'year', 'exam', 'answers']
        model = Question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'exam', 'year', 'month', 'subject', 'question', 'option_1', 'option_2', 'option_3', 'option_4', 'answer' ]
        model = Answer