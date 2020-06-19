import os
import dj_database_url
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'app',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': '',
        'HOST': 'host',
        'PORT': '',
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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

IMAGE_URL = '/images/'
IMAGE_ROOT = os.path.join(BASE_DIR, 'images')

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTH_USER_MODEL = 'accounts.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# 2020年の祝日
PUBLIC_HOLIDAYS = [
    datetime.date(year=2020, month=1, day=1),
    datetime.date(year=2020, month=1, day=13),
    datetime.date(year=2020, month=2, day=11),
    datetime.date(year=2020, month=2, day=23),
    datetime.date(year=2020, month=2, day=24),
    datetime.date(year=2020, month=3, day=20),
    datetime.date(year=2020, month=4, day=29),
    datetime.date(year=2020, month=5, day=3),
    datetime.date(year=2020, month=5, day=4),
    datetime.date(year=2020, month=5, day=5),
    datetime.date(year=2020, month=7, day=20),
    datetime.date(year=2020, month=8, day=11),
    datetime.date(year=2020, month=9, day=21),
    datetime.date(year=2020, month=9, day=22),
    datetime.date(year=2020, month=10, day=12),
    datetime.date(year=2020, month=11, day=3),
    datetime.date(year=2020, month=11, day=23),
]

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']
    import django_heroku
    django_heroku.settings(locals()) 