from django.contrib import admin
from .models import CGPA   # <== This is the correct model

admin.site.register(CGPA)
