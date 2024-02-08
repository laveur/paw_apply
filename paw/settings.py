"""
Django settings for paw project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.pacanthro.org',
    '.moltenvisuals.com',
    'localhost'
]


# Application definition

INSTALLED_APPS = [
    'core.apps.CoreConfig',
    'console.apps.ConsoleConfig',
    'dancecomp.apps.DancecompConfig',
    'merchants.apps.MerchantsConfig',
    'panels.apps.PanelsConfig',
    'partyfloor.apps.PartyfloorConfig',
    'performers.apps.PerformersConfig',
    'volunteers.apps.VolunteersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sendgrid',
    'crispy_forms',
    'crispy_bootstrap5'
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

ROOT_URLCONF = 'paw.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'emails/merchants'),
            os.path.join(BASE_DIR, 'emails/panels'),
            os.path.join(BASE_DIR, 'emails/partyfloor'),
            os.path.join(BASE_DIR, 'emails/performers'),
            os.path.join(BASE_DIR, 'emails/volunteers'),
        ],
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

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_FAIL_SILENTLY = not DEBUG

# Email Config
EMAIL_BACKEND = 'sgbackend.SendGridBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
EMAIL_DOMAIN = os.getenv('EMAIL_DOMAIN') or 'pacanthro.org'
DEFAULT_FROM_EMAIL = 'noreply@'+EMAIL_DOMAIN
MERCHANT_EMAIL = 'merchant@'+EMAIL_DOMAIN
PANEL_EMAIL = 'panel@'+EMAIL_DOMAIN
VOLUNTEER_EMAIL = 'volunteer@'+EMAIL_DOMAIN
PERFORMERS_EMAIL = 'dj@'+EMAIL_DOMAIN
HOTEL_EMAIL = 'hotel@'+EMAIL_DOMAIN
DANCE_EMAIL = 'dancecomp@'+EMAIL_DOMAIN

WSGI_APPLICATION = 'paw.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': 'paw_apply',
        'USER': os.getenv('PG_USER'),
        'PASSWORD': os.getenv('PG_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

LOGIN_URL = 'console:login'


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]
