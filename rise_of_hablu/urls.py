# rise_of_hablu/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rehablu.urls')),  # Already added
    path('', include('rehablu.urls')),      # Include rehablu URLs at the root as well
]