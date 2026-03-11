"""
Module for note-related forms.
Defines the structure for creating and updating sticky notes.
"""

from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating sticky notes."""

    class Meta:
        """Metadata for NoteForm."""

        model = Note
        fields = [
            'title',
            'content',
            'color',
        ]
