from rest_framework import serializers
from .models import Exam, Year, Month, Subject, Question, Answer

class ExamSerializer(serializers.ModelSerializer):
    years = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='year-detail')
    
    def get_years_count(self, obj):
        obj.name_count

    class Meta:
        model = Exam
        fields = ['id', 'name', 'years']

class YearSerializer(serializers.ModelSerializer):
    months = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='month-detail')

    class Meta:
        model = Year
        fields = ['id','months', 'year', 'exam']

    def to_representation(self, instance):
        rep = super(YearSerializer, self).to_representation(instance)
        rep['exam'] = instance.exam.name
        return rep


class MonthSerializer(serializers.ModelSerializer):
    subjects = serializers.HyperlinkedRelatedField(
        view_name='subject-detail',
        # lookup_field='name',
        many=True, 
        read_only=True
        )


    class Meta:
        model = Month
        fields = ['id', 'name', 'subjects', 'year', 'exam']

    def to_representation(self, instance):
        rep = super(MonthSerializer, self).to_representation(instance)
        rep['exam'] = instance.exam.name
        rep['year'] = instance.year.year
        return rep       


class SubjectSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='question-detail')
    
    class Meta:
        fields = ['id', 'name', 'month', 'year', 'exam', 'questions']
        model = Subject

    def to_representation(self, instance):
        rep = super(SubjectSerializer, self).to_representation(instance)
        rep['month'] = instance.month.name
        rep['year'] = instance.year.year
        rep['exam'] = instance.exam.name
        return rep


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='answer-detail')

    class Meta:
        fields = ['id', 'question_text', 'subject', 'month', 'year', 'exam', 'answers']
        model = Question

    def to_representation(self, instance):
        rep = super(QuestionSerializer, self).to_representation(instance)
        rep['subject'] = instance.subject.name
        rep['month'] = instance.month.name
        rep['year'] = instance.year.year
        rep['exam'] = instance.exam.name
        return rep 


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'exam', 'year', 'month', 'subject', 'question', 'option_1', 'option_2', 'option_3', 'option_4', 'answer' ]
        model = Answer

    def to_representation(self, instance):
        rep = super(AnswerSerializer, self).to_representation(instance)
        rep['question'] = instance.question.question_text
        rep['subject'] = instance.subject.name
        rep['month'] = instance.month.name
        rep['year'] = instance.year.year
        rep['exam'] = instance.exam.name
        return rep 