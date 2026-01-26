import openpyxl
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404  # Додано get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import ZVT, Schedule


def get_filtered_zvt(request):
    """Утиліта для пошуку та фільтрації"""
    items = ZVT.objects.all()
    search_query = request.GET.get('search', '').strip()
    department_filter = request.GET.get('department', '')
    status_filter = request.GET.get('status', '')
    today = timezone.now().date()

    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(serial_number__icontains=search_query) |
            Q(organization__icontains=search_query) |
            Q(manufacturer__icontains=search_query)
        )

    if department_filter:
        items = items.filter(department=department_filter)

    stats_items = items

    if status_filter == 'overdue':
        items = items.filter(next_check_date__lt=today)
    elif status_filter == 'ok':
        items = items.filter(next_check_date__gte=today)

    return items.order_by('name'), search_query, department_filter, status_filter, stats_items


@login_required
def export_zvt_excel(request):
    """Функція генерації Excel"""
    items, _, _, _, _ = get_filtered_zvt(request)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Журнал ЗВТ"

    columns = [
        '№ п/п', 'Назва ЗВТ', 'Дільниця', 'Заводський №',
        'Організація, що повіряє', 'Дата повірки', 'Наступна повірка'
    ]
    ws.append(columns)

    for index, obj in enumerate(items, start=1):
        ws.append([
            index,
            obj.name,
            obj.department,
            obj.serial_number,
            obj.organization,
            obj.last_check_date.strftime('%d.%m.%Y') if obj.last_check_date else '',
            obj.next_check_date.strftime('%d.%m.%Y') if obj.next_check_date else ''
        ])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Journal_ZVT.xlsx'
    wb.save(response)
    return response


@login_required
def journal_list(request):
    """Головна сторінка """
    items, search_query, department_filter, status_filter, stats_items = get_filtered_zvt(request)
    today = timezone.now().date()

    overdue_count = stats_items.filter(next_check_date__lt=today).count()
    ok_count = stats_items.filter(next_check_date__gte=today).count()

    departments = ZVT.objects.exclude(Q(department="") | Q(department__isnull=True)).values_list('department',
                                                                                                 flat=True).distinct()
    all_schedules = Schedule.objects.all().order_by('-uploaded_at')

    context = {
        'items': items,
        'overdue_count': overdue_count,
        'ok_count': ok_count,
        'departments': sorted(departments),
        'search_query': search_query,
        'department_filter': department_filter,
        'status_filter': status_filter,
        'all_schedules': all_schedules,
    }
    return render(request, 'registry/list.html', context)


# --- НОВА ФУНКЦІЯ ДЛЯ ПЕРЕХОДУ НА СТОРІНКУ ХАРАКТЕРИСТИК ---

@login_required
def zvt_detail(request, pk):
    """Сторінка з детальними характеристиками конкретного ЗВТ"""
    # Шукаємо прилад за первинним ключем (ID)
    item = get_object_or_404(ZVT, pk=pk)

    context = {
        'item': item,
    }
    return render(request, 'registry/detail.html', context)