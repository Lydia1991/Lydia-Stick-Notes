"""Module for registering models with the Django admin interface."""
from django.contrib import admin
from .models import Note

admin.site.register(Note)
