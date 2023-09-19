"""
Django settings for barter project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from configurations import Configuration, values
from pathlib import Path
import os

class Dev(Configuration):
# Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-(c-1scd%j+t1x9o))z&j_%oe4xdtd)mesz+i%ybw%0ten@%6gs'
    SECRET_KEY = values.SecretValue()
    print(SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

# ALLOWED_HOSTS = []
    ALLOWED_HOSTS = values.ListValue([], separator=';')
    CSRF_TRUSTED_ORIGINS = values.ListValue([], separator=';')
    CORS_ALLOWED_ORIGINS = values.ListValue([], separator=';')

# Application definition

    INSTALLED_APPS = [
        # Disable django static file handling
        'whitenoise.runserver_nostatic',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.gis',
        # Cors
        'corsheaders',
        'cities',
        'rest_framework',
        'rest_framework_simplejwt',
        'rest_framework_gis',
        'drf_yasg',
        # versatileimagefield
        'versatileimagefield',
        # Django-Filter
        'django_filters',
        # OAuth
        'oauth2_provider',
        'social_django',
        'drf_social_oauth2',
        # Verify email
        'verify_email.apps.VerifyEmailConfig',
        # Main App
        'trade',
    ]

    MIDDLEWARE = [
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        # 'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    STORAGE = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

    ROOT_URLCONF = 'barter.urls'
    LOGIN_URL = 'login'
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
                    # OAuth
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'barter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('SQL_ENGINE', 'django.contrib.gis.db.backends.postgis'),
            'NAME': os.environ.get('POSTGRES_NAME'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': os.environ.get('POSTGRES_HOST', 'db'),
            'PORT': os.environ.get('POSTGRES_PORT', 5432),
        }
    }

    CLIENT_URL = values.Value('http://localhost:3000')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

    AUTH_USER_MODEL = 'trade.User'
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

    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend"
        ],
        # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 50,
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
            # OAuth
            'oauth2_provider.contrib.rest_framework.OAuth2Authentication',  # django-oauth-toolkit >= 1.0.0
            'drf_social_oauth2.authentication.SocialAuthentication',
        ]
    }
    # DRF-SOCIAL-OAUTH2
    AUTHENTICATION_BACKENDS = (
        # Google  OAuth2
        'social_core.backends.google.GoogleOAuth2',
        # drf-social-oauth2
        'drf_social_oauth2.backends.DjangoOAuth2',
        # Django
        'django.contrib.auth.backends.ModelBackend',
    )
    # DRFSO2_PROPRIETARY_BACKEND_NAME = 'Django'
    # DRFSO2_URL_NAMESPACE = ''
    # ACTIVATE_JWT = False
    # Google configuration
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "<your app id goes here>"
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "<your app secret goes here>"
    from datetime import timedelta
    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=600),
    }

    # Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
    SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
    ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
    STATIC_URL = values.Value('/static/')
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # WHITENOISE_STATIC_PREFIX = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    print('MEDIA_ROOT: ', MEDIA_ROOT)

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SWAGGER_SETTINGS = {
        "SECURITY_DEFINITIONS": {
            "token": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            },
        },
    }

    LOGGING = {
        'version': 1,
        'filters': {
            'require_debug_true': {
                '()': 'django.utils.log.RequireDebugTrue',
            }
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'filters': ['require_debug_true'],
                'class': 'logging.StreamHandler',
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'DEBUG',
                'handlers': ['console'],
            }
        }
    }

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


class Prod(Dev):
    """
    The in-production settings.
    """

    DOTENV = os.path.join(Dev.BASE_DIR, '.env.dev')
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.environ.get('EMAIL_ID') 
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PW')