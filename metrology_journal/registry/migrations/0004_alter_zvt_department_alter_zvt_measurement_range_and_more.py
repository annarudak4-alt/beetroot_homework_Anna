from django.db import migrations, models

class Migration(migrations.Migration):
    """
        Четверта міграція проєкту (0004_alter_zvt_department_alter_zvt_measurement_range_and_more).
        Мета змінити параметри деяких полів моделі ZVT
        для підвищення гнучкості або виправлення помилок.
    """
    dependencies = [
        ('registry', '0003_schedule_alter_zvt_department_alter_zvt_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zvt',
            name='department',
            field=models.CharField(max_length=100, verbose_name='Дільниця'),
        ),
        migrations.AlterField(
            model_name='zvt',
            name='measurement_range',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Межі вимірювання'),
        ),
        migrations.AlterField(
            model_name='zvt',
            name='zvt_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип'),
        ),
    ]
