from pathlib import Path

# Путь к корню проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Безопасность
SECRET_KEY = 'django-insecure-e(i(__#&5p57c0i!9%o6-p!9wp6k(!#wgl!(jj-+mzg$p=++%e'
DEBUG = True
ALLOWED_HOSTS = []

# 🔹 Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'shop',

    'bboard',   # твое существующее приложение
    # 'accounts', # добавляем наше приложение с страницами
]

# 🔹 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔹 Корневой urls.py
ROOT_URLCONF = 'samplesite.urls'

# 🔹 Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # шаблоны внутри apps
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🔹 WSGI
WSGI_APPLICATION = 'samplesite.wsgi.application'

# 🔹 База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔹 Валидация пароля
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Локализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_TZ = True

# 🔹 Статика
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # добавляем папку static

# 🔹 Primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
