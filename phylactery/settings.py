"""
Django settings for phylactery project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from django.contrib.messages import constants as messages
from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'taggit',
    'dal',
    'dal_select2',
    'members.apps.MembersConfig',
    'library.apps.LibraryConfig',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'django.contrib.postgres',
    'markdownify',
    'django_celery_beat',
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

ROOT_URLCONF = 'phylactery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'phylactery/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'phylactery.context_processors.navbar_colour_settings',
                'phylactery.context_processors.unigames_user_processor',
                'phylactery.context_processors.domain_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'phylactery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/phylactery/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'phylactery/static')
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# Email Settings
# Remember to set these in local_settings
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

LOGIN_URL = 'account:login'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Dragon related colour settings:
# NAVBAR_THEME: Can either be 'light' or 'dark'.
# Use light for light background colours and dark for dark background colours.
# NAVBAR_COLOUR: The colour of the navbar you want.
NAVBAR_THEME = 'dark'
NAVBAR_COLOUR = '#911f71 '

TAGGIT_CASE_INSENSITIVE = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    messages.INFO: 'alert-info',
    messages.ERROR: 'alert-danger',
    messages.WARNING: 'alert-warning',
    messages.DEBUG: 'alert-warning',
    messages.SUCCESS: 'alert-success',
}


MARKDOWNIFY_STRIP = False
MARKDOWNIFY_WHITELIST_TAGS = [
    'a', 'p',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7',
    'ul', 'li', 'span', 'ol',
    'em', 'strong', 'pre', 'code', 'blockquote'
]

# Celery Stuff
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Australia/Perth'

JAZZMIN_SETTINGS = {
    'show_ui_builder': False,
    'site_title': 'Unigames Admin',
    'site_header': 'Unigames Admin',
    'site_brand': 'Unigames Admin',
    'welcome_sign': 'Welcome to the Unigames Admin Panel. Please Log In.',
    'copyright': 'Unigames',
    'site_logo': 'phylactery/images/unigames_admin_logo.png',
    'custom_css': 'jazzmin/css/additional.css',
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "library.Item": "fas fa-book",
        "library.BorrowRecord": 'fas fa-receipt',
        "library.ExternalBorrowingForm": 'fas fa-file-import',
        "library.TagParent": 'fas fa-tags',
        'members.Member': 'fas fa-user',
        'members.Membership': 'fas fa-user-check',
        'members.Rank': 'fas fa-graduation-cap',
        'members.Memberflag': 'fas fa-user-tag',
        'django_celery_beat.PeriodicTask': 'fas fa-calendar-check',
        'django_celery_beat.ClockedSchedule': 'fas fa-clock',
        'django_celery_beat.CrontabSchedule': 'fas fa-calendar-alt',
        'django_celery_beat.IntervalSchedule': 'fas fa-hourglass-half',
        'django_celery_beat.SolarSchedule': 'fas fa-sun',
        'taggit.Tag': 'fas fa-tag',
        'sites.Site': 'fas fa-globe',
        'blog.BlogPost': 'fas fa-newspaper',
        'blog.EmailOrder': 'fas fa-paper-plane',
    },
    'order_with_respect_to': [
        'members', 'members.Member', 'members.Membership', 'members.MemberFlag', 'members.Rank',
        'auth', 'auth.User', 'auth.Group',
        'library', 'library.Item', 'library.BorrowRecord', 'library.ExternalBorrowingForm', 'library.TagParents',
        'blog', 'blog.BlogPost', 'blog.EmailOrder',
        'taggit',
        'django_celery_beat', 'django_celery_beat.PeriodicTask',
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "lumen",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary text-dark",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
}

try:
    with open(os.path.join(os.path.dirname(__file__), 'local_settings.py')) as f:
        exec(f.read(), globals())
except IOError:
    pass

