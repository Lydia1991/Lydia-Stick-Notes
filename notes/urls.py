"""URL configuration for the notes application."""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteListView.as_view(), name='note_list'),
    path('note/new/', views.NoteCreateView.as_view(), name='note_create'),
    path(
        'note/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'
    ),
    path(
        'note/<int:pk>/update/',
        views.NoteUpdateView.as_view(),
        name='note_update'
    ),
    path(
        'note/<int:pk>/delete/',
        views.NoteDeleteView.as_view(),
        name='note_delete'
    ),
    path(
        'note/<int:pk>/toggle/',
        views.toggle_note_complete,
        name='note_toggle'
    ),
]
