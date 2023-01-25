from django.db import models

# Create your models here.
class Exam(models.Model):
  name = models.CharField(max_length = 255, unique=True)
  
  class Meta:
    verbose_name_plural = "Exams"
    ordering = ['id']
  
  def __str__(self):
    return self.name

  
class Year(models.Model):
  year = models.CharField(max_length=255)
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='years')

  
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
    return f'{self.name} - {self.year}'
		
class Subject(models.Model):
  SUBJECTS = [
    ('General Mathematics', 'General Mathematics'),
    ('Further Mathematics', 'Further Mathematics'),
    ('English Language', 'English Language'),
    ('Economics', 'Economics'),
    ('Physics', 'Physics'),
    ('Biology', 'Biology'),
    ('Chemistry', 'Chemistry'),
    ('Geography', 'Geography'),
    ('Government', 'Government'),
    ('Commerce', 'Commerce'),
    ('Accounting', 'Accounting'),
    ('History', 'History'),
    ('Agricultural Science', 'Agricultural Science'),
    ('Management', 'Management'),
    ('Civics', 'Civics'),
    ('Computer Science', 'Computer Science'),
    ('Marketing', 'Marketing'),
    ('English Literature', 'English Literature'),
    ('Islamic Studies', 'Islamic Studies'),
    ('Christian Religious Studies', 'Christian Religious Studies'),
    ('Hausa', 'Hausa'),
    ('Igbo', 'Igbo'),
    ('Yoruba', 'Yoruba')
  ]
  name = models.CharField(max_length = 255, choices=SUBJECTS)
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, related_name='subjects')
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name='subjects')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='subjects')
  
  class Meta:
    verbose_name_plural = "Subjects"
    ordering = ['exam', 'year']

  def __repr__(self) -> str:
    print(self)
    return super().__repr__()

  def __str__(self):
    return self.name

  
class Question(models.Model):
  question_text = models.TextField(db_index=True)
  subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, related_name='questions')
  month = models.ForeignKey(Month, on_delete=models.DO_NOTHING, related_name='questions')
  year = models.ForeignKey(Year, on_delete=models.DO_NOTHING, related_name='questions')
  exam = models.ForeignKey(Exam, on_delete=models.DO_NOTHING, related_name='questions')
  
  @property
  def counts(self):
    questions = self.Objects.all()
    return len(questions)
  
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
