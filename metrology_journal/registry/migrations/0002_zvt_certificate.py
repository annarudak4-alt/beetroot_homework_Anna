
from django.db import migrations, models


class Migration(migrations.Migration):
    """
        Друга міграція проєкту (0002_zvt_certificate).
        Додає до моделі ZVT нове поле 'certificate' для зберігання
        скан-копії сертифіката засобу вимірювальної техніки.
        """
    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zvt',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to='certificates/%Y/', verbose_name='Скан-копія сертифіката'),
        ),
    ]
