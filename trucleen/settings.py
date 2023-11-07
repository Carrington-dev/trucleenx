from pathlib import Path
import os
from django.contrib import messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(^81031l!mx!_9#bj*_#838!m$+khie0dnxo)r_auf=lin*o%7'

DEBUG = True

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "myauth",
    "contact",
    "book",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trucleen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myauth.context_processors.show_me',
            ],
        },
    },
]

WSGI_APPLICATION = 'trucleen.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = "myauth.NewUser"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]




MESSAGE_TAGS = {
    messages.DEBUG : 'alert-info',
    messages.INFO : 'alert-info',
    messages.SUCCESS : 'alert-success',
    messages.WARNING : 'alert-warning',
    messages.ERROR : 'alert-danger',
}
CRISPY_TEMPLATE_PACK = 'bootstrap4'
GRAPPELLI_ADMIN_TITLE = "Stemgon Softwares"
LOG_FILE = os.path.join(BASE_DIR,  'logs/stderr.log')

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}


DJANGORESIZED_DEFAULT_SIZE = [1920, 1080]
DJANGORESIZED_DEFAULT_SCALE = 1
DJANGORESIZED_DEFAULT_QUALITY = 75
DJANGORESIZED_DEFAULT_KEEP_META = True
DJANGORESIZED_DEFAULT_FORCE_FORMAT = 'JPEG'
DJANGORESIZED_DEFAULT_FORMAT_EXTENSIONS = {'JPEG': ".jpg"}
DJANGORESIZED_DEFAULT_NORMALIZE_ROTATION = True
SITE_ID = 1

ADMINS = 'crn96m@gmail.com'
SECURE_CROSS_ORIGIN_OPENER_POLICY='same-origin-allow-popups'
#CSRF_TRUSTED_ORIGINS = ["https://stemgon.online", "https://www.stemgon.online"]

# EMAIL_PORT = 465
# EMAIL_USE_SSL = True
# EMAIL_HOST = 'server145.web-hosting.com'
# EMAIL_HOST_USER = 'contact@stemgon.online'
# EMAIL_HOST_PASSWORD = '#Mulalo96'
# DEFAULT_FROM_EMAIL = 'Trucleen <contact@stemgon.online>'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

GRAPPELLI_ADMIN_TITLE = "Stemgon Softwares"
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_PASSWORD = '#Mulalo96'
EMAIL_HOST_USER = 'admin@mytuta.co.za'
DEFAULT_FROM_EMAIL = 'Trucleen <admin@mytuta.co.za>'