from django.test import TestCase
from django.utils import timezone
from datetime import date, timedelta
from .models import ZVT


class ZVTModelTest(TestCase):
    def setUp(self):
        """Налаштування даних для тестів"""
        self.today = date.today()

        # 1. Прилад, повірка якого була сьогодні (період 12 міс)
        self.zvt_ok = ZVT.objects.create(
            name="Манометр",
            department="Цех 1",
            manufacturer="Еталон",
            serial_number="A123",
            zvt_type="МП-4",
            measurement_range="0-10 МПа",
            check_period=12,
            last_check_date=self.today,
            organization="ДП Тест",
            conclusion="придатний"
        )

        # 2. Прилад, повірка якого закінчується через 10 днів
        self.zvt_soon = ZVT.objects.create(
            name="Термометр",
            department="Цех 2",
            serial_number="B456",
            check_period=6,
            last_check_date=self.today - timedelta(days=170),  # Майже 6 місяців тому
            next_check_date=self.today + timedelta(days=10),
            conclusion="придатний"
        )

    def test_next_check_date_calculation(self):
        """Перевірка автоматичного розрахунку дати"""
        # 12 місяців ~ 360 днів у нашій моделі (self.check_period * 30)
        expected_date = self.zvt_ok.last_check_date + timedelta(days=360)
        self.assertEqual(self.zvt_ok.next_check_date, expected_date)

    def test_is_soon_logic(self):
        """Перевірка статусу 'Скоро повірка' (менше 30 днів)"""
        self.assertTrue(self.zvt_soon.is_soon())
        self.assertFalse(self.zvt_ok.is_soon())

    def test_is_overdue_logic(self):
        """Перевірка статусу 'Протерміновано'"""
        # Створюємо протермінований прилад
        overdue_zvt = ZVT.objects.create(
            name="Ваги",
            department="Склад",
            serial_number="C789",
            check_period=12,
            last_check_date=date(2023, 1, 1),
            next_check_date=date(2024, 1, 1),
            conclusion="придатний"
        )
        self.assertTrue(overdue_zvt.is_overdue())


class ZVTViewTest(TestCase):
    def test_journal_list_view(self):
        """Перевірка доступності головної сторінки для користувача"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Електронний журнал")
