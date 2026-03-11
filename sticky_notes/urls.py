"""
Main URL Configuration for the sticky_notes project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Path for the Django Admin interface
    path('admin/', admin.site.urls),

    # Core application paths: Connects the root URL to your notes app
    path('', include('notes.urls')),
]
