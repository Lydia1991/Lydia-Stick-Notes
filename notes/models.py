"""Module for sticky note data models."""
from django.db import models


class Note(models.Model):
    """Model representing a 3x3 sticky note."""

    COLOR_CHOICES = [
        ('#fff382', 'Yellow'),
        ('#ffc1cc', 'Pink'),
        ('#b2fab4', 'Green'),
        ('#b3e5fc', 'Blue'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    color = models.CharField(
        max_length=7, choices=COLOR_CHOICES, default='#fff382'
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return the note title."""
        return self.title
