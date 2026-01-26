from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.db.models import QuerySet
import openpyxl
from .models import ZVT, Schedule
from typing import cast, Any

@admin.register(ZVT)
class ZVTAdmin(admin.ModelAdmin):
    actions = ['export_selected_to_excel']

    # Налаштування відображення списку (додано контроль креслення)
    list_display = ('name', 'serial_number', 'department', 'next_check_date', 'status_colored', 'has_certificate', 'has_drawing')
    list_filter = ('department', 'conclusion')
    search_fields = ('name', 'serial_number', 'department')

    # ОНОВЛЕНО: Форма редагування з новими полями
    fieldsets = (
        ('Основна інформація', {
            'fields': ('name', 'zvt_type', 'manufacturer', 'serial_number', 'department', 'description')
        }),
        ('Технічна документація', {  # НОВИЙ РОЗДІЛ
            'fields': ('control_dimensions', 'technical_drawing'),
            'description': 'Параметри для контролю та технічні креслення приладу'
        }),
        ('Метрологія', {
            'fields': (
                'measurement_range',
                'last_check_date',
                'check_period',
                'next_check_date',
                'organization',
                'conclusion',
                'certificate'
            )
        }),
    )

    readonly_fields = ()

    @admin.display(description='Скан', boolean=True)
    def has_certificate(self, obj: ZVT) -> bool:
        return bool(obj.certificate)

    # Додано індикатор наявності креслення у списку
    @admin.display(description='Креслення', boolean=True)
    def has_drawing(self, obj: ZVT) -> bool:
        return bool(obj.technical_drawing)

    @admin.display(description='Статус терміну')
    def status_colored(self, obj: ZVT):
        if not obj.next_check_date:
            return mark_safe('<span style="color: gray;">Не вказано</span>')

        if obj.is_overdue():
            return mark_safe('<span style="color: #dc2626; font-weight: bold;">⚠️ ПРОТЕРМІНОВАНО</span>')
        if obj.is_soon():
            return mark_safe('<span style="color: #d97706; font-weight: bold;">⏳ СКОРО (30 днів)</span>')

        return mark_safe('<span style="color: #16a34a; font-weight: bold;">✅ ОК</span>')

    @admin.action(description='Завантажити вибрані в Excel')
    def export_selected_to_excel(self, _request, queryset: QuerySet[ZVT]):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Експорт ЗВТ"
        # Можна додати контрольну колонку в експорт, якщо потрібно
        ws.append(['Назва ЗВТ', 'Заводський №', 'Дільниця', 'Дата наступної повірки', 'Заключення', 'Контр. розміри'])

        for obj in queryset:
            date_str = obj.next_check_date.strftime('%d.%m.%Y') if obj.next_check_date else "Не вказано"
            ws.append([
                obj.name,
                obj.serial_number,
                obj.department,
                date_str,
                obj.get_conclusion_display(),
                obj.control_dimensions or ""
            ])

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Export_Metmag.xlsx"'
        wb.save(cast(Any, response))
        return response

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'get_file_link')
    list_filter = ('uploaded_at',)
    search_fields = ('title',)

    @admin.display(description='Посилання на файл')
    def get_file_link(self, obj):
        if obj.file:
            return mark_safe(f'<a href="{obj.file.url}" target="_blank">📄 Відкрити файл</a>')
        return "Файл відсутній"