# rehablu/serializers.py

from rest_framework import serializers
from .models import SubjectGrade

class SubjectGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectGrade
        fields = '__all__'
