from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from rest_framework.decorators import action
from django.contrib.auth.hashers import check_password
from rest_framework import status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import base64
from django.utils import timezone



from .serializers import *

from .models import *
from datetime import datetime, timedelta

# Create your views here.

# Path: quizeapp/coaching/views.py

class CoachingViewSet(viewsets.ModelViewSet):
    queryset = Coaching.objects.all()
    serializer_class = CoachingSerializer
    model = Coaching
    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = Coaching.objects.all()
        serializer = CoachingSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CoachingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CoachingSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CoachingSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

       
class CoachingStudentsViewSet(viewsets.ModelViewSet):
    queryset = CoachingStudents.objects.all()
    serializer_class = CoachingStudentsSerializer
    model = CoachingStudents
    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = CoachingStudents.objects.all()
        serializer = CoachingStudentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CoachingStudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CoachingStudentsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CoachingStudentsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer
    model = Subjects
    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = Subjects.objects.all()
        serializer = SubjectsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = SubjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubjectsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubjectsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




class QuestionPaperViewset(viewsets.ModelViewSet):
    queryset = QuestionPaper.objects.all()
    serializer_class = QuestionPaperSerializer
    model = QuestionPaper
    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = QuestionPaper.objects.all()
        serializer = QuestionPaperSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CreateQuestionPaperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = QPRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CreateQuestionPaperSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    model = Test
    # permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = Test.objects.all()
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        test = Test.objects.create( name=data['name']+" Test",
                                    coaching_id=data['coaching'],
                                    subject_id=data['subject'],
                                    question_paper_id=data['id'],
                                    user_id='dc62f033-876b-4291-bb6d-086312ea06ab',
                                    total_marks=data['total_marks'],
                                    obtained_marks=0,
                                    date=datetime.now().date(),
                                    time=data['time'],
                                    )

        test_result_details = []
        marks = 0
        for question in data['questions']:
            question_obj = Questions.objects.get(id=question['id'])
            
            user_ans = getattr(question_obj, question['answer']) if question['answer'] else "not_answered"
            correct_ans = getattr(question_obj, question_obj.answer)
          

            test_result_details.append(TestResultDetails(   test_id=test.id,
                                                            question_id=question['id'],
                                                            user_answer=user_ans,
                                                            correct_answer=correct_ans,
                                                            is_correct="not_answered" if not question['answer'] else "correct" if question_obj.answer == question['answer'] else "incorrect",
                                                    )
                                    )
            if question_obj.answer == question['answer']:
              
                marks += question_obj.marks
        test.obtained_marks = marks
        test.save()
        TestResultDetails.objects.bulk_create(test_result_details)
        return Response({"message":"Test Completed."},status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TestSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        # instance = self.get_object()
        # serializer = CreateTestSerializer(instance, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # print(serializer.errors)
        # return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
          return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=False, methods=['get'])
    def get_test_result(self, request):
        test_id = request.query_params.get('test_id')
        try:
            test = Test.objects.get(id=test_id)
        except:
            return Response({"message":"Test not found."},status=status.HTTP_400_BAD_REQUEST)
        test_result_details = TestResultDetails.objects.filter(test_id=test_id)
        serializer = TestResultDetailsSerializer(test_result_details, many=True)
        return Response({"test": TestSerializer(test).data, "test_result_details": serializer.data}, status=status.HTTP_200_OK)