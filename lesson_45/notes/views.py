from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm
from asgiref.sync import sync_to_async

@login_required
async def notes_list(request):
    user = await request.auser()

    # Використовуємо sync_to_async, щоб безпечно витягнути список із категоріями
    # Це вирішує помилку SynchronousOnlyOperation у шаблонах
    def get_notes_sync():
        return list(Note.objects.filter(user=user).select_related('category').order_by('-id'))

    notes = await sync_to_async(get_notes_sync)()
    return render(request, 'notes/index.html', {'notes': notes})

@login_required
async def create_note(request):
    user = await request.auser()
    if request.method == "POST":
        form = NoteForm(request.POST)
        is_valid = await sync_to_async(form.is_valid)()
        if is_valid:
            note = await sync_to_async(form.save)(commit=False)
            note.user = user
            await sync_to_async(note.save)()
            return redirect('home')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form, 'title': 'Створити нотатку'})

@login_required
async def edit_note(request, pk):
    user = await request.auser()
    # Використовуємо aget для асинхронного пошуку
    note = await Note.objects.aget(pk=pk, user=user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        is_valid = await sync_to_async(form.is_valid)()
        if is_valid:
            await sync_to_async(form.save)()
            return redirect('home')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {
        'form': form,
        'note': note,
        'title': 'Редагувати нотатку'
    })

@login_required
async def delete_note(request, pk):
    user = await request.auser()
    note = await Note.objects.aget(pk=pk, user=user)
    if request.method == "POST":
        await note.adelete()
        return redirect('home')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})