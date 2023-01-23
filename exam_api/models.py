from django.db import models

# Create your models here.
class Exam(models.Model):
  name = models.CharField(max_length = 255, unique=True)

  @property
  def years_count(self):
    return self.name.count()
  
  class Meta:
    verbose_name_plural = "Exams"
    ordering = ['id']
  
  def __str__(self):
    return self.name

  
class Year(models.Model):
  year = models.IntegerField()
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='years')

  @property
  def months_count(self):
    return self.months.count()
  
  class Meta:
    verbose_name_plural = "Years"
    ordering = ['id']
  
  def __str__(self):
    return f'{self.year} - {self.exam.name}'


  
class Month(models.Model):
  MONTHS = [
    ('MAY/JUN','MAY/JUNE'),
    ('JUN/JUL','JUNE/JULY'),
    ('OCT/NOV', 'OCTOBER/NOVEMBER'),
    ('Others', 'Others'),
  ]
  name = models.CharField(max_length = 20, choices=MONTHS)
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name='months')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='months')
  
  class Meta:
    verbose_name_plural = "Months"
    ordering = ['id']

  def __str__(self):
    return self.name
		
class Subject(models.Model):

  name = models.CharField(max_length = 255)
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, related_name='subjects')
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name='subjects')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='subjects')
  
  class Meta:
    verbose_name_plural = "Subjects"
    ordering = ['id']

  def __str__(self):
    return self.name

  
class Question(models.Model):
  question_text = models.TextField(db_index=True)
  subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name='questions')
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, related_name='questions')
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name='questions')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='questions')
  
  
  class Meta:
    verbose_name_plural = "Questions"
    ordering = ['id']
  
  def __str__(self):
    return self.question_text

  
class Answer(models.Model):
  option_1 = models.CharField(max_length=255, default=None )
  option_2 = models.CharField(max_length=255, default=None )
  option_3 = models.CharField(max_length=255, default=None )
  option_4 = models.CharField(max_length=255, default=None )
  answer = models.CharField(max_length=255, default=None )
  # correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.DO_NOTHING,  related_name='answers')
  subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING,  related_name='answers')
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, related_name='answers')
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name='answers')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='answers')

  
  class Meta:
    verbose_name_plural = "Answers"
    ordering = ['id']

  def __str__(self):
    return self.answer
