from django.db import models

class CGPA(models.Model):
    semester = models.CharField(max_length=50)
    gpa = models.FloatField()

class SubjectGrade(models.Model):
    subject = models.CharField(max_length=100)
    grade = models.IntegerField()
    
    def __str__(self):
        return f'{self.semester} - {self.gpa}'
