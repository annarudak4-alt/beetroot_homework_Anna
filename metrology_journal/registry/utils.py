from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import ZVT


def send_check_reminders():
    # Визначаємо дату через 30 днів від сьогодні
    target_date = timezone.now().date() + timedelta(days=30)

    # Шукаємо прилади, у яких наступна повірка саме в цей день
    upcoming_zvt = ZVT.objects.filter(next_check_date=target_date)

    if upcoming_zvt.exists():
        subject = f"Нагадування: Повірка ЗВТ через 30 днів ({target_date})"

        message = "Список приладів, термін повірки яких закінчується через місяць:\n\n"
        for item in upcoming_zvt:
            message += f"- {item.name} (Зав. №{item.serial_number}), Дільниця: {item.department}\n"

        send_mail(
            subject,
            message,
            'metrology-system@company.com',
            ['metrolog@company.com'],  # Пошта метролога
            fail_silently=False,
        )
        return f"Надіслано сповіщень: {upcoming_zvt.count()}"
    return "Приладів для повірки не знайдено."
