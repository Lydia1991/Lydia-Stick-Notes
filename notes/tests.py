"""
Unit tests for the Sticky Notes application.
Covers Model creation, List view, Detail view, and Update functionality.
"""
from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteProjectTests(TestCase):
    """Test suite for Note models and views."""

    def setUp(self):
        """Create a sample note for testing."""
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content",
            color="#fff382"
        )

    def test_note_content(self):
        """1. Verify the note data is saved correctly."""
        self.assertEqual(self.note.title, "Test Note")

    def test_list_view(self):
        """2. Verify the dashboard loads (Status 200)."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        """3. Verify the detail page for a specific note works."""
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)

    def test_update_note(self):
        """4. Verify that updating a note changes its title in the database."""
        new_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'color': '#ffc1cc'
        }
        # Send a POST request to the update URL
        self.client.post(reverse('note_update', args=[self.note.id]), new_data)

        # Refresh from database and check if title changed
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')
