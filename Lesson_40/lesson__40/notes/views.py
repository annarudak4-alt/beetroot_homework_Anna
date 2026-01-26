from django.shortcuts import render
from .models import Note, Category

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