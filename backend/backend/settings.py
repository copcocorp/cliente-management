import os
from pathlib import Path
import dj_database_url
import pymysql
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# PyMySQL como MySQLdb
pymysql.install_as_MySQLdb()

# BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY y DEBUG
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dev-key-only')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS
if not DEBUG:
    ALLOWED_HOSTS = [
        os.environ.get('RAILWAY_DOMAIN', 'cliente-management-production.up.railway.app'),
        'cliente-administracion.netlify.app'
    ]
else:
    ALLOWED_HOSTS = ['*']

# INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'clientes',
    'whitenoise.runserver_nostatic',
]

# MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# DATABASES
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'clientes_db'),
            'USER': os.environ.get('DB_USER', 'root'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', '3306'),
            'OPTIONS': {'charset': 'utf8mb4'},
        }
    }

# PASSWORD VALIDATORS
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# LOCALIZATION
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
}

# CORS
#CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "https://cliente-administracion.netlify.app",  # tu frontend en Netlify
]

CORS_ALLOW_CREDENTIALS = True
CORS_REPLACE_HTTPS_REFERER = True


# SEGURIDAD EN PRODUCCIÓN
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = False  # Evita redirecciones infinitas
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_TRUSTED_ORIGINS = [
        f"https://{os.environ.get('RAILWAY_DOMAIN')}",
        "https://cliente-administracion.netlify.app"
    ]
