from django.db import models

from .constants import ANSWER_STATUS_CHOICES

from .utils import PrimaryUUIDTimeStampedModel

from django.conf import settings

# Create your models here.


"""
Coaching model
Subjects
question_papers
questions
test
test_result
test_result_details
coaching_students

"""

class Coaching(PrimaryUUIDTimeStampedModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='coaching_logo',null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Subjects(PrimaryUUIDTimeStampedModel):
    coaching = models.ForeignKey(Coaching, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class QuestionPaper(PrimaryUUIDTimeStampedModel):
    coaching = models.ForeignKey(Coaching, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_marks = models.IntegerField()
    time = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Questions(PrimaryUUIDTimeStampedModel):
    coaching = models.ForeignKey(Coaching, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return self.question

class Test(PrimaryUUIDTimeStampedModel):
    name = models.CharField(max_length=100,null=False,blank=False,default='Test')
    coaching = models.ForeignKey(Coaching, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    date = models.DateField()
    time = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name




class TestResultDetails(PrimaryUUIDTimeStampedModel):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)
    is_correct = models.CharField(max_length=100, choices=ANSWER_STATUS_CHOICES, default="not_answered")

    def __str__(self):
        return self.question.question

class CoachingStudents(PrimaryUUIDTimeStampedModel):
    coaching = models.ForeignKey(Coaching, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.coaching.name+" - "+self.user.name