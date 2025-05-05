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

