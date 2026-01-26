from django.core.management.base import BaseCommand
from registry.utils import send_check_reminders

class Command(BaseCommand):
    help = 'Надсилає Email-сповіщення про терміни повірки'

    def handle(self, *args, **options):
        result = send_check_reminders()
        self.stdout.write(self.style.SUCCESS(result))
