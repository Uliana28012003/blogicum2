# Импорт нужных модулей для работы с путями
from pathlib import Path
import os

# Базовая директория проекта (используется для построения других путей)
BASE_DIR = Path(__file__).resolve().parent.parent

# Настройки для статики
STATIC_URL = '/static/'  # URL по которому будут доступны статические файлы (css, js, картинки)
STATICFILES_DIRS = [BASE_DIR / 'static']  # Указываем, где хранятся статические файлы в проекте

# Секретный ключ (используется Django для безопасности: подписи, сессии и т.д.)
SECRET_KEY = 'django-insecure-3@l&wu*-kppk%-j3)1+@#q&ye@-rfn=8d@l%d^$a@%m)3)7*4s'

# Включаем режим отладки (True — для разработки, False — для продакшена)
DEBUG = True

# Список разрешённых хостов (в продакшене сюда добавляются домены сайта)
ALLOWED_HOSTS = []

# Приложения, подключённые к проекту
INSTALLED_APPS = [
    'django.contrib.admin',            # Панель администратора
    'django.contrib.auth',             # Система аутентификации
    'django.contrib.contenttypes',     # Типы моделей (контент)
    'django.contrib.sessions',         # Поддержка сессий
    'django.contrib.messages',         # Система сообщений
    'django.contrib.staticfiles',      # Поддержка статики
    'pages',                           # Твоё приложение для инфо-страниц
    'blog',                            # Твоё приложение с постами
]

# Промежуточные слои (middleware) — они обрабатывают запросы и ответы
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Защита от CSRF-атак
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Главный файл маршрутов (urls.py проекта)
ROOT_URLCONF = 'blogicum.urls'

# Указываем путь до папки с шаблонами
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

# Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Шаблонизатор Django
        'DIRS': [TEMPLATES_DIR],  # Папка, где искать шаблоны (например, templates/blog/index.html)
        'APP_DIRS': True,         # Ищет шаблоны в папках внутри приложений
        'OPTIONS': {
            'context_processors': [  # Дополнительные переменные, доступные в шаблонах
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI — точка входа для сервера (не трогаем)
WSGI_APPLICATION = 'blogicum.wsgi.application'

# Настройки базы данных — SQLite (по умолчанию)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Тип БД
        'NAME': BASE_DIR / 'db.sqlite3',         # Файл базы данных
    }
}

# Валидаторы паролей (работают при регистрации/изменении пароля)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Настройки языка и времени
LANGUAGE_CODE = 'en-us'  # Язык интерфейса
TIME_ZONE = 'UTC'        # Часовой пояс

USE_I18N = True  # Интернационализация (переводы)
USE_L10N = True  # Локализация (форматы дат и чисел)
USE_TZ = True    # Использование часового пояса

# Настройка автоматического поля ID в моделях
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
