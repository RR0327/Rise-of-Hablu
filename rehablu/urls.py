# rehablu/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectGradeViewSet

router = DefaultRouter()
router.register(r'subjectgrades', SubjectGradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
