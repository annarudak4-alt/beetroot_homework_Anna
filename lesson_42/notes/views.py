from django.shortcuts import render
from .models import Note, Category
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

def notes_list(request):
    # 1. Наповнення тестовими даними (якщо база порожня)
    if not Category.objects.exists():
        cat = Category.objects.create(title="Невікладні справи")
        Note.objects.create(
            title="Домашні справи",
            text="Прибирання, прання",
            category=cat
        )
        Note.objects.create(
            title="Покупки",
            text="Кава, чай, яблука",
            category=cat
        )

    # 2. Отримання даних з БД
    notes = Note.objects.all()

    return render(request, 'notes/index.html', {'notes': notes})

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Створити нотатку'})

# Редагування та деталі
def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form, 'note': note, 'title': 'Редагувати нотатку'})

# Видалення
def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})