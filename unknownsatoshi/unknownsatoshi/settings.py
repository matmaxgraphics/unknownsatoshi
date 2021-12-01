
from pathlib import Path
import os
import environ
import django_heroku

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if DEBUG == False:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'blog'
LOGOUT_REDIRECT_URL = 'home'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #local apps
    'cms',
    'userprolog',

    # for rich text field
    'ckeditor',
    'ckeditor_uploader',

    #cloudinary modul
    'cloudinary',
    'cloudinary_storage',
]


# ck editor configuration
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source', 'Image', 'Update', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak']
        ]
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'unknownsatoshi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'unknownsatoshi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASS'),
#         'HOST': env('DB_HOST'),
#         'PORT': env('DB_PORT'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# cloudinary config

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": env("cloud_name"),
    "API_KEY": env("api_key"),
    "API_SECRET": env("api_secret"),
}

# cloudinary configuration for image uploads
#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# django error logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'my_log_handler': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['my_log_handler'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    },
}


# mailing smtp configuration
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("HOST")
EMAIL_PORT = 587
USE_TLS = True
USER_SSL = False
EMAIL_HOST_USER = env("USER")
EMAIL_HOST_PASSWORD = env("PASSWORD")
DEFAULT_FROM_EMAIL = env("FROM_EMAIL")


# flutterwave payment gateway configuration
#for production
FLW_PRODUCTION_PUBLIC_KEY = env("FLW_PRODUCTION_PUBLIC_KEY")
FLW_PRODUCTION_SECRET_KEY = env("FLW_PRODUCTION_SECRET_KEY")
FLW_PRODUCTION_ENCRYPTION_KEY=env("FLW_PRODUCTION_ENCRYPTION_KEY")

#for test
FLW_SANDBOX_PUBLIC_KEY = env("FLW_SANDBOX_PUBLIC_KEY")
FLW_SANDBOX_SECRET_KEY = env("FLW_SANDBOX_SECRET_KEY")
FLW_SANDBOX_ENCRYPTION_KEY=env("FLW_SANDBOX_ENCRYPTION_KEY")
FLW_SANDBOX = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'userprolog.User'

django_heroku.settings(locals())

