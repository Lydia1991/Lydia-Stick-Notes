"""
Module containing views for CRUD operations and search for sticky notes.
This follows PEP 257 docstring standards.
"""

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Note


class NoteListView(ListView):
    """View to display a searchable horizontal grid of sticky notes."""

    model = Note
    template_name = 'notes/note_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        """Filter notes by title or content if a query 'q' exists."""
        queryset = Note.objects.all().order_by('-updated_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        return queryset


class NoteDetailView(DetailView):
    """View to display the full content of a specific sticky note."""

    model = Note
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    """View to handle the creation of a new sticky note."""

    model = Note
    fields = ['title', 'content', 'color']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')


class NoteUpdateView(UpdateView):
    """View to handle editing an existing note."""

    model = Note
    fields = ['title', 'content', 'color']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('note_list')


class NoteDeleteView(DeleteView):
    """View to confirm and execute deletion."""

    model = Note
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')


def toggle_note_complete(request, pk):
    """Toggles the 'is_completed' status of a note."""
    note = get_object_or_404(Note, pk=pk)
    note.is_completed = not note.is_completed
    note.save()
    return redirect('note_list')
