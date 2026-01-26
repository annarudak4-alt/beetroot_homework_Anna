from django.db import models
from django.utils import timezone
from datetime import timedelta, date


class ZVT(models.Model):
    CONCLUSION_CHOICES = [
        ('придатний', 'Придатний'),
        ('непридатний', 'Непридатний'),
    ]

    name = models.CharField("Назва ЗВТ", max_length=255)
    department = models.CharField("Дільниця", max_length=100)
    manufacturer = models.CharField("Завод виготовлювач", max_length=255)
    serial_number = models.CharField("Заводський номер", max_length=100)

    # Опис приладу
    description = models.TextField("Опис приладу", blank=True, null=True)

    # НОВІ ПОЛЯ: Контрольні розміри та Схема
    control_dimensions = models.TextField("Контрольні розміри", blank=True, null=True)
    technical_drawing = models.FileField(
        "Схема / Креслення",
        upload_to='drawings/%Y/',
        blank=True,
        null=True
    )

    zvt_type = models.CharField("Тип", max_length=100, blank=True, null=True)
    measurement_range = models.CharField("Межі вимірювання", max_length=100, blank=True, null=True)

    check_period = models.IntegerField("Період перевірки (місяців)")
    last_check_date = models.DateField("Дата перевірки")

    next_check_date = models.DateField("Дата наступної перевірки", blank=True, null=True)

    organization = models.CharField("Організація, що виконує перевірку", max_length=255)
    conclusion = models.CharField("Заключення", max_length=20, choices=CONCLUSION_CHOICES)

    certificate = models.FileField(
        "Скан-копія сертифіката",
        upload_to='certificates/%Y/',
        blank=True,
        null=True
    )

    def is_overdue(self):
        if not self.next_check_date: return False
        return date.today() > self.next_check_date

    def is_soon(self):
        if not self.next_check_date: return False
        delta = self.next_check_date - date.today()
        return 0 <= delta.days <= 30

    def save(self, *args, **kwargs):
        if not self.next_check_date and self.last_check_date and self.check_period:
            days_to_add = int(self.check_period * 30.44)
            self.next_check_date = self.last_check_date + timedelta(days=days_to_add)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

    class Meta:
        verbose_name = "Засіб вимірювальної техніки"
        verbose_name_plural = "Засоби вимірювальної техніки"


class Schedule(models.Model):
    title = models.CharField("Назва документа (напр. Графік на 2026 рік)", max_length=255)
    file = models.FileField("Файл графіка (PDF/Excel)", upload_to='schedules/%Y/')
    uploaded_at = models.DateTimeField("Дата завантаження", auto_now_add=True)

    class Meta:
        verbose_name = "Графік повірки"
        verbose_name_plural = "Графіки повірки"
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.title