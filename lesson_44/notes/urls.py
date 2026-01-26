from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='home'),
    path('note/new/', views.create_note, name='note_create'),
    path('note/<int:pk>/edit/', views.edit_note, name='note_edit'),
    path('note/<int:pk>/delete/', views.delete_note, name='note_delete'),
]