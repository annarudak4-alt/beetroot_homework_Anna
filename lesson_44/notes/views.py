from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

@login_required
def notes_list(request):
    """Показує лише нотатки поточного користувача"""
    notes = Note.objects.filter(user=request.user).order_by('-id')
    return render(request, 'notes/index.html', {'notes': notes})

@login_required
def create_note(request):
    """Створює нотатку та автоматично призначає автора"""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # Прив'язка до юзера
            note.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Створити нотатку'})

@login_required
def edit_note(request, pk):
    """Дозволяє редагувати лише свою нотатку (захист через user=request.user)"""
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'note': note, 'title': 'Редагувати нотатку'})

@login_required
def delete_note(request, pk):
    """Дозволяє видалити лише свою нотатку"""
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})