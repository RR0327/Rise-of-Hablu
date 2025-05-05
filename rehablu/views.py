# Phase 1: Create a Django app named "rehablu" and set up the models

# rehablu/views.py

from rest_framework import viewsets
from .models import SubjectGrade
from .serializers import SubjectGradeSerializer

class SubjectGradeViewSet(viewsets.ModelViewSet):
    queryset = SubjectGrade.objects.all()
    serializer_class = SubjectGradeSerializer

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
