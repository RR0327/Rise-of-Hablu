# Phase 1: 
# Feature 1: Create a Django model for CGPA and Subject Grade

from rest_framework import viewsets
from .models import SubjectGrade, LearnNewSkill, DressBetter
from .serializers import SubjectGradeSerializer, LearnNewSkillSerializer, DressBetterSerializer

class SubjectGradeViewSet(viewsets.ModelViewSet):
    queryset = SubjectGrade.objects.all()
    serializer_class = SubjectGradeSerializer

# Feature 2: Learn new skills

from rest_framework import viewsets
from .models import LearnNewSkill
from .serializers import LearnNewSkillSerializer

class LearnNewSkillViewSet(viewsets.ModelViewSet):
    queryset = LearnNewSkill.objects.all()
    serializer_class = LearnNewSkillSerializer

# PHASE 2 

# Feature 2: Dress Better

class DressBetterViewSet(viewsets.ModelViewSet):
    queryset = DressBetter.objects.all()
    serializer_class = DressBetterSerializer

# Phase 3: Career & Brain Boosters (3 Features)
# Feature 1: Find a Job

from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Feature 2: Pick a Movie

from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Feature 3: Random Fun Fact

from .models import FunFact
from .serializers import FunFactSerializer

class FunFactViewSet(viewsets.ModelViewSet):
    queryset = FunFact.objects.all()
    serializer_class = FunFactSerializer

# Phase 4: Hero Dashboard

from rest_framework import viewsets, permissions
from .models import StudyGroup, HeroDashboard
from .serializers import StudyGroupSerializer, HeroDashboardSerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

class HeroDashboardViewSet(viewsets.ModelViewSet):
    queryset = HeroDashboard.objects.all()
    serializer_class = HeroDashboardSerializer
    