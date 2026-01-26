from django.test import TestCase, Client
from django.urls import reverse
from .models import Note, Category


class NoteViewsTest(TestCase):
    def setUp(self):
        # 1. Готуємо дані для тестів
        self.client = Client()
        self.category = Category.objects.create(title="Тест Категорія")
        self.note = Note.objects.create(
            title="Тестова нотатка",
            text="Текст",
            category=self.category
        )

    def test_delete_note_view(self):
        # 2. Використовуємо правильне ім'я 'note_delete' з вашого urls.py
        url = reverse('note_delete', args=[self.note.pk])

        # 3. Виконуємо запит на видалення
        response = self.client.post(url)

        # 4. Перевіряємо результат
        self.assertEqual(Note.objects.count(), 0)
        self.assertRedirects(response, reverse('home'))

    def test_edit_note_view(self):
        # Додатковий тест на редагування (використовуємо 'note_edit')
        url = reverse('note_edit', args=[self.note.pk])
        response = self.client.post(url, {
            'title': 'Оновлена назва',
            'text': 'Оновлений текст',
            'category': self.category.id
        })
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Оновлена назва')