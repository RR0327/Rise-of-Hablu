# rehablu/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SubjectGradeViewSet, JobViewSet, MovieViewSet, FunFactViewSet,
    StudyGroupViewSet, HeroDashboardViewSet
)

router = DefaultRouter()

# Phase 1
router.register(r'subjectgrades', SubjectGradeViewSet)

# Phase 3
router.register(r'jobs', JobViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'funfacts', FunFactViewSet)

# Phase 4
router.register(r'studygroups', StudyGroupViewSet)
router.register(r'herodashboard', HeroDashboardViewSet, basename='herodashboard')

urlpatterns = [
    path('', include(router.urls)),
]
