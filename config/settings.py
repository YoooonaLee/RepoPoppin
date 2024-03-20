"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import json
import environ
import dj_database_url

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY_DJANGO')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "mysite-wfiz.onrender.com", "backend-o6c1.onrender.com", "backend.pop-pin.store",]


# Application definition

CUSTOM_APPS = [
    'common.apps.CommonConfig',
    'users.apps.UsersConfig',
    'stores.apps.StoresConfig',
    'reviews.apps.ReviewsConfig',
    'wishlists.apps.WishlistsConfig',
    'reports.apps.ReportsConfig',
    'accesslogs.apps.AccesslogsConfig',
    'topstores.apps.TopstoresConfig',
]

SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
]

INSTALLED_APPS = CUSTOM_APPS + SYSTEM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",

]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'mydata2',
        'USER':  'encore',
        'PASSWORD' : env('SECRET_PW'),
        'HOST' : '52.78.92.36',
        'PORT':  '3306',
        'OPTIONS': {'charset': 'utf8mb4'},                      
            }}

# if DEBUG:
#     DATABASES = {'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME':  'mydata2',
#             'USER':  'encore',
#             'PASSWORD' : env('SECRET_PW'),
#             'HOST' : '52.78.92.36',
#             'PORT':  '3306'                      
#             }}
# else:
#     DATABASES = {
#         "default": dj_database_url.config(
#             conn_max_age=600,
#         )
#     }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':  'mydata2',
#         'USER':  'encore',
#         'PASSWORD' : env('SECRET_PW'),
#         'HOST' : '52.78.92.36',
#         'PORT':  '3306'                      
#         }}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'users.User'

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAGE_SIZE = 9
REVIEW_SIZE = 10

# APPEND_SLASH = False

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "config.authentication.TrustMeBroAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "config.authentication.JWTAuthentication",
    ]
}

if DEBUG:
    CORS_ALLOWED_ORIGINS = ["http://127.0.0.1:3000"]
    CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:3000"]
else:
    CORS_ALLOWED_ORIGINS = ["https://pop-pin.store"]
    CSRF_TRUSTED_ORIGINS = ["https://pop-pin.store"]
CORS_ALLOW_CREDENTIALS = True

if not DEBUG:
    SESSION_COOKIE_DOMAIN = ".pop-pin.store"
    CSRF_COOKIE_DOMAIN = ".pop-pin.store"
    


GH_SECRET = env('GH_SECRET')