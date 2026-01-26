
import os
from pathlib import Path
from dotenv import load_dotenv

# Шлях до кореневої папки проєкту
BASE_DIR = Path(__file__).resolve().parent.parent

# Завантаження змінних з .env
load_dotenv(os.path.join(BASE_DIR, '.env'))

# --- ОСНОВНІ НАЛАШТУВАННЯ ---
SECRET_KEY = os.getenv('SECRET_KEY')

# Перетворюємо рядок 'True'/'False' з .env на логічний тип
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Отримуємо хости зі списку, розділеного комами
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# --- ЗАСТОСУНКИ ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registry',  # Ваша програма
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# --- БАЗА ДАНИХ ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- ЛОКАЛІЗАЦІЯ ---
LANGUAGE_CODE = 'uk'
TIME_ZONE = 'Europe/Kyiv'
USE_I18N = True
USE_TZ = True

# --- СТАТИКА ТА МЕДІА ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- НАЛАШТУВАННЯ EMAIL (Через .env) ---
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- ДОДАНО ДЛЯ АВТОРИЗАЦІЇ METMAG ---
LOGIN_REDIRECT_URL = 'journal_list'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_URL = 'login'