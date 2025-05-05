# rehablu/views.py

from rest_framework import viewsets
from .models import SubjectGrade
from .serializers import SubjectGradeSerializer

class SubjectGradeViewSet(viewsets.ModelViewSet):
    queryset = SubjectGrade.objects.all()
    serializer_class = SubjectGradeSerializer
