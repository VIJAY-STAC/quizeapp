from rest_framework import serializers
from .models import *

class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaching
        fields = ('id','name', 'address', 'contact','email','website','logo')



class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('id','coaching', 'name', 'description')

class QuestionPaperSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name')
    class Meta:
        model = QuestionPaper
        fields = ('id','coaching', 'subject', 'name', 'description', 'total_marks', 'time', 'is_active')

class CreateQuestionPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionPaper
        fields = ('id','coaching', 'subject', 'name', 'description', 'total_marks', 'time', 'is_active')

class QuestionsSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name')
    class Meta:
        model = Questions
        fields = ('id','coaching', 'subject', 'question_paper', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks')


class QPRetrieveSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    class Meta:
        model = QuestionPaper
        fields = ('id','coaching', 'subject', 'name', 'total_marks', 'time', 'questions')

    def get_questions(self, obj):
        qs = Questions.objects.filter(question_paper=obj.id)
        return QuestionsSerializer(qs, many=True).data

    

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id','coaching', 'subject', 'question_paper', 'user', 'total_marks', 'date', 'time', 'is_active','obtained_marks')


class MiniQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = ('question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks')

class TestResultDetailsSerializer(serializers.ModelSerializer):
    question = MiniQuestionsSerializer()
    class Meta:
        model = TestResultDetails
        fields = ('question', 'user_answer','correct_answer')


class CoachingStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingStudents
        fields = ('id','coaching', 'user', 'is_active')