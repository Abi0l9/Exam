from django.db import models

# Create your models here.
class Exam(models.Model):
  name = models.CharField(max_length = 255)
  
  class Meta:
    verbose_name_plural = "Exams"
    ordering = ['id']
  
  def __str__(self):
    return self.name

  
class Year(models.Model):
  year = models.IntegerField()
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
  
  class Meta:
    verbose_name_plural = "Years"
    ordering = ['id']
  
  def __str__(self):
    return self.year

  
class Month(models.Model):
  name = models.CharField(max_length = 255)
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING)
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
  
  class Meta:
    verbose_name_plural = "Months"
    ordering = ['id']

  def __str__(self):
    return self.name
		
class Subject(models.Model):
  name = models.CharField(max_length = 255)
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING)
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING)
  exam_name = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
  
  class Meta:
    verbose_name_plural = "Subjects"
    ordering = ['id']

  def __str__(self):
    return self.name

  
class Question(models.Model):
  question_text = models.TextField()
  subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING)
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING)
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
  
  class Meta:
    verbose_name_plural = "Questions"
    ordering = ['id']
  
  def __str__(self):
    return self.question_text

  
class Answer(models.Model):
  answer = models.CharField(max_length=255)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
  subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING)
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING)
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING)
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING)
  
  class Meta:
    verbose_name_plural = "Answers"
    ordering = ['id']

  def __str__(self):
    return self.answer
