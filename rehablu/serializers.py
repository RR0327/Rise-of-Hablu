# Phase 1: Create a Django model for CGPA and Subject Grade

from rest_framework import serializers
from .models import SubjectGrade

class SubjectGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectGrade
        fields = '__all__'
        read_only_fields = ('grade_point',)  # Prevent external write

# Phase 3: Career & Brain Boosters (3 Features)
# Feature 1: Find a Job

from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

# Feature 2: Pick a Movie

from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# Feature 3: Random Fun Fact

from .models import FunFact

class FunFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunFact
        fields = '__all__'

# Phase 4: Hero Dashboard

from rest_framework import serializers
from .models import StudyGroup, HeroDashboard

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'

class HeroDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroDashboard
        fields = ['full_name', 'email', 'phone', 'title']  # <-- Only valid model fields here!
        
# Chatbot
from rest_framework import serializers
from .models import OpenAIChat

class OpenAIChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = OpenAIChat
        fields = '__all__'
        read_only_fields = ('created_at',)


# run hablu run
from rest_framework import serializers
from .models import Marathon

class MarathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marathon
        fields = '__all__'
