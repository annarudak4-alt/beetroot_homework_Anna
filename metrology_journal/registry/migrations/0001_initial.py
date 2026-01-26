
from django.db import migrations, models
class Migration(migrations.Migration):
    """
        Початкова міграція
        Створює таблицю для моделі ZVT
    """
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZVT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Перелік ЗВТ')),
                ('department', models.CharField(max_length=100, verbose_name='Дільниця')),
                ('manufacturer', models.CharField(max_length=255, verbose_name='Завод виготовлювач')),
                ('serial_number', models.CharField(max_length=100, verbose_name='Заводський номер')),
                ('zvt_type', models.CharField(max_length=100, verbose_name='Тип')),
                ('measurement_range', models.CharField(max_length=100, verbose_name='Межі вимірювання')),
                ('check_period', models.IntegerField(verbose_name='Період перевірки (місяців)')),
                ('last_check_date', models.DateField(verbose_name='Дата перевірки')),
                ('next_check_date', models.DateField(blank=True, null=True, verbose_name='Дата наступної перевірки')),
                ('organization', models.CharField(max_length=255, verbose_name='Організація, що виконує перевірку')),
                ('conclusion', models.CharField(choices=[('придатний', 'Придатний'), ('непридатний', 'Непридатний')], max_length=20, verbose_name='Заключення')),
            ],
            options={
                'verbose_name': 'Засіб вимірювальної техніки',
                'verbose_name_plural': 'Засоби вимірювальної техніки',
            },
        ),
    ]
