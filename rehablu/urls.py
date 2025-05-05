# rehablu/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectGradeViewSet, JobViewSet, MovieViewSet, FunFactViewSet

router = DefaultRouter()

# Phase 1
router.register(r'subjectgrades', SubjectGradeViewSet)

# Phase 3
router.register(r'jobs', JobViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'funfacts', FunFactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
