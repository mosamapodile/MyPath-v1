import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================================
# CORE DEVELOPMENT ENVIRONMENT BASICS
# ==========================================
SECRET_KEY = 'django-insecure-mypath-hackathon-development-key-2026'
DEBUG = False # CRUCIAL: Always set to False in production for security hardening
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# CRUCIAL: Directs incoming requests to the master routing configuration
ROOT_URLCONF = 'config.urls'

# Database configuration using standard SQLite3 backend layout
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 1. Register our applications cleanly
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-Party Dependencies
    'rest_framework',
    'rest_framework.authtoken',  # CRUCIAL: Enables database-backed auth tokens
    'corsheaders',

    # Custom Core Modules
    'apps.authentication',
    'apps.academics',
    'apps.career_ai',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Crucial for admin
    'corsheaders.middleware.CorsMiddleware',                  # For frontend API connection
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Crucial for admin/auth
    'django.contrib.messages.middleware.MessageMiddleware',    # Crucial for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 2. Inform Django to utilize our custom extending user object model
AUTH_USER_MODEL = 'authentication.User'

# ==========================================
# REST FRAMEWORK & CORS ARCHITECTURE KEYS
# ==========================================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', # Instructs DRF to parse bearer tokens
    ],
}

# Allows your frontend server running on port 5173 to execute API requests
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

# 3. Configure Broker Channels for Async tasks (Celery + Redis)
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# ==========================================
# STATIC FILES CONFIGURATION
# ==========================================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'