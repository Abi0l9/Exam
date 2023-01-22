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
  title = models.ForeignKey(Exam, on_delete=models.DO_NOTHING,
  related_name='exam_name')
  
  class Meta:
		verbose_name_plural = "Years"
		ordering = ['id']
  
  def __str__(self):
		return self.year

  
class Month(models.Model):
  name = models.CharField(max_length = 255)
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING,
  related_name='exam_year')
  title = models.ForeignKey(Exam, on_delete=models.DO_NOTHING,
  related_name='exam_name')
  
  class Meta:
		verbose_name_plural = "Months"
		ordering = ['id']

  def __str__(self):
		return self.name

  
class Question(models.Model):
  question_text = models.TextField()
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING,
  related_name='exam_year')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING,
  related_name='exam_name')
  
  class Meta:
		verbose_name_plural = "Questions"
		ordering = ['id']
  
  def __str__(self):
		return self.question_text

  
class Answer(models.Model):
  answer = models.charField(max_length=255)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,
  related_name='question')
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING,
  related_name='exam_year')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING,
  related_name='exam_name')
  
  class Meta:
		verbose_name_plural = "Answers"
		ordering = ['id']

  def __str__(self):
		return self.answer
