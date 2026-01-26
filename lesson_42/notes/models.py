from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст нотатки")
    reminder = models.DateTimeField(null=True, blank=True, verbose_name="Нагадування")
    # Зовнішній ключ для зв'язку з категорією
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return self.title