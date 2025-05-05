# Phase 1: Create a Django model for CGPA and Subject Grade

from django.db import models

class CGPA(models.Model):
    semester = models.CharField(max_length=50)
    gpa = models.FloatField()

class SubjectGrade(models.Model):
    subject = models.CharField(max_length=100)
    grade = models.FloatField()

    def __str__(self):
        return f'{self.semester} - {self.gpa}'

# Phase 3: Career & Brain Boosters (3 Features)

# Feature 1: Find a Job

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()

    def __str__(self):
        return f"{self.title} at {self.company}"

# Feature 2: Pick a Movie

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

# Feature 3: Random Fun Fact

class FunFact(models.Model):
    fact = models.TextField()

    def __str__(self):
        return self.fact[:50]  # first 50 chars

# Phase 4: Hero Dashboard

# Study Group Planner Model
class StudyGroup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# Hero Dashboard Model (Example stats/info of user)

# rehablu/models.py

from django.db import models

class HeroDashboard(models.Model):
    full_name = models.CharField(max_length=255, default='Unknown')
    email = models.EmailField(default="example@example.com")
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
    
# Chatbot
from django.db import models
class OpenAIChat(models.Model):
    messages = models.TextField()  # Stores the conversation history
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Chat {self.id}"

# run hablu run

from django.db import models

class Marathon(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    top_participant = models.CharField(max_length=100)

    def __str__(self):
        return self.name
