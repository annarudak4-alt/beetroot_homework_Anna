from django.urls import path
from django.contrib.auth import views as auth_views
from .views import journal_list, export_zvt_excel, zvt_detail # Додано zvt_detail

urlpatterns = [
    # Головна сторінка - веде на СПИСОК
    path('', journal_list, name='journal_list'),

    # Сторінка експорту - веде на ЗАВАНТАЖЕННЯ ЕКСЕЛЬ
    path('export/', export_zvt_excel, name='export_zvt_excel'),

    # Детальна сторінка приладу - перехід за ID (pk)
    path('zvt/<int:pk>/', zvt_detail, name='zvt_detail'),

    # МАРШРУТИ АВТОРИЗАЦІЇ
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]