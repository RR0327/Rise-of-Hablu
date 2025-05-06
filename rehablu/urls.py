# rehablu/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from .views import (
    SubjectGradeViewSet, JobViewSet, MovieViewSet, FunFactViewSet,
    StudyGroupViewSet, HeroDashboardViewSet, LearnNewSkillViewSet, DressBetterViewSet, OpenAIChatViewSet, MarathonViewSet
)

router = DefaultRouter()

# Phase 1
router.register(r'subjectgrades', SubjectGradeViewSet)
router.register(r'learnskills', LearnNewSkillViewSet)

# Phase 2
router.register(r'dressbetter', DressBetterViewSet)

# Phase 3
router.register(r'jobs', JobViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'funfacts', FunFactViewSet)

# Phase 4
router.register(r'studygroups', StudyGroupViewSet)
router.register(r'herodashboard', HeroDashboardViewSet, basename='herodashboard')

# Chatbots
# router.register(r'chatbot', OpenAIChatViewSet, basename='chatbot')

#Run Hablu, Run
router.register(r'marathon', MarathonViewSet, basename='marathon')

urlpatterns = [
    path('', include(router.urls)),
    path('subject_grades/', TemplateView.as_view(template_name='subject_grades.html')),
    path('learn_skills/', TemplateView.as_view(template_name='learn_skills.html')),
    path('dress_better/', TemplateView.as_view(template_name='dress_better.html')),
    path('jobs/', TemplateView.as_view(template_name='jobs.html')),
    path('movies/', TemplateView.as_view(template_name='movies.html')),
    path('fun_facts/', TemplateView.as_view(template_name='fun_facts.html')),
    path('study_groups/', TemplateView.as_view(template_name='study_groups.html')),
    path('hero_dashboard/', TemplateView.as_view(template_name='hero_dashboard.html')),
    path('chatbot/', TemplateView.as_view(template_name='chatbot.html')),
    path('marathons/', TemplateView.as_view(template_name='marathons.html')),
    path('home/', TemplateView.as_view(template_name='home.html')),
    path('add_subject_grade/', TemplateView.as_view(template_name='add_subject_grade.html')),
    path('add_learn_skill/', TemplateView.as_view(template_name='add_learn_skill.html')),
    path('add_dress_better/', TemplateView.as_view(template_name='add_dress_better.html')),
    path('add_fun_fact/', TemplateView.as_view(template_name='add_fun_fact.html')),
    path('add_study_group/', TemplateView.as_view(template_name='add_study_group.html')),
    path('add_hero_dashboard/', TemplateView.as_view(template_name='add_hero_dashboard.html')),
]