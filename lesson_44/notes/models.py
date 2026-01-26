from django.conf import settings
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.title

class Note(models.Model):
    # Додаємо зв'язок з користувачем
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name="Автор"
    )
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст нотатки")
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Нагадування")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes', verbose_name="Категорія")

    def __str__(self):
        return self.title