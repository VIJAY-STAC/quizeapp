from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"coaching",CoachingViewSet,basename="coaching")
router.register(r"subjects",SubjectsViewSet,basename="subjects")
router.register(r"questionpaper",QuestionPaperViewset,basename="questionpaper")
# router.register(r"questions",QuestionsViewSet,basename="users")
router.register(r"test",TestViewSet,basename="users")
# router.register(r"testresult",TestResultViewSet,basename="users")
# router.register(r"testresultdetails",TestResultDetailsViewSet,basename="users")
router.register(r"coachingstudents",CoachingStudentsViewSet,basename="users")
urlpatterns = [
    path('api/v3/',include(router.urls))
  
]