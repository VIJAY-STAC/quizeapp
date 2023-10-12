from django.contrib import admin
from .models import Coaching, Subjects, QuestionPaper, Questions, Test, TestResultDetails, CoachingStudents

# Register your models here.
admin.site.register(Coaching)
class CoachingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact','email','website','logo')
    list_filter = ('name', 'address', 'contact','email','website','logo')

admin.site.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('coaching', 'name', 'description')
    list_filter = ('coaching', 'name', 'description')

admin.site.register(QuestionPaper)
class QuestionPaperAdmin(admin.ModelAdmin):
    list_display = ('coaching', 'subject', 'name', 'description', 'total_marks', 'time', 'is_active')
    list_filter = ('coaching', 'subject', 'name', 'description', 'total_marks', 'time', 'is_active')

admin.site.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('coaching', 'subject', 'question_paper', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks')
    list_filter = ('coaching', 'subject', 'question_paper', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks')

admin.site.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('coaching', 'subject', 'question_paper', 'user', 'total_marks', 'date', 'time', 'is_active')
    list_filter = ('coaching', 'subject', 'question_paper', 'user', 'total_marks', 'date', 'time', 'is_active')


admin.site.register(TestResultDetails)
class TestResultDetailsAdmin(admin.ModelAdmin):
    list_display = ['test', 'question', 'user_answer', 'correct_answer', 'is_correct']

    # Make one column (e.g., 'question') a clickable link to the detail view
    list_display_links = ['question']

admin.site.register(CoachingStudents)
class CoachingStudentsAdmin(admin.ModelAdmin):
    list_display = ('coaching', 'user', 'is_active')
    list_filter =  ('coaching', 'user', 'is_active')

