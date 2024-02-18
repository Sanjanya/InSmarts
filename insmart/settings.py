import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qihh1lz*%@wsa!c47y5fp#!z=uyjzu1d@)3sxjs1e@#_w=kocc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIREBASE_SERVICE_ACCOUNT_KEY_PATH = os.path.join(BASE_DIR, 'keys', 'C:/Users/sanju/insmart/Keys/insmarts-ca6eb-firebase-adminsdk-xjga2-802eef073e.json')

cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_KEY_PATH)
firebase_admin.initialize_app(cred)

# ...

FIREBASE_API_KEY = "AIzaSyASU0Vl7RKpzxFwF9rbeF5o58RL3tyagqs"
FIREBASE_AUTH_DOMAIN = "insmarts-ca6eb.firebaseapp.com"
FIREBASE_DATABASE_URL = "https://insmarts-ca6eb-default-rtdb.firebaseio.com"
FIREBASE_PROJECT_ID = "insmarts-ca6eb"
FIREBASE_STORAGE_BUCKET = "insmarts-ca6eb.appspot.com"
FIREBASE_MESSAGING_SENDER_ID = "892860860379"
FIREBASE_APP_ID = "1:892860860379:web:69d51eaae434f0972289fe"
FIREBASE_MEASUREMENT_ID = "G-1T0PBP64GK"

# Add Firebase to Django settings
firebase_config = {
    "apiKey": FIREBASE_API_KEY,
    "authDomain": FIREBASE_AUTH_DOMAIN,
    "databaseURL": FIREBASE_DATABASE_URL,
    "projectId": FIREBASE_PROJECT_ID,
    "storageBucket": FIREBASE_STORAGE_BUCKET,
    "messagingSenderId": FIREBASE_MESSAGING_SENDER_ID,
    "appId": FIREBASE_APP_ID,
    "measurementId": FIREBASE_MEASUREMENT_ID,
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)

# Add Firebase to Django
os.environ['FIREBASE_CONFIG'] = json.dumps(firebase_config)
admin.site.firebase = firebase

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
    'news',
    'firebase',
    'firebase-admin',
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

ROOT_URLCONF = 'insmart.urls'

FIREBASE_API_KEY = firebase_config.FIREBASE_API_KEY
FIREBASE_AUTH_DOMAIN = firebase_config.FIREBASE_AUTH_DOMAIN
FIREBASE_DATABASE_URL = firebase_config.FIREBASE_DATABASE_URL
FIREBASE_PROJECT_ID = firebase_config.FIREBASE_PROJECT_ID
FIREBASE_STORAGE_BUCKET = firebase_config.FIREBASE_STORAGE_BUCKET
FIREBASE_MESSAGING_SENDER_ID = firebase_config.FIREBASE_MESSAGING_SENDER_ID
FIREBASE_APP_ID = firebase_config.FIREBASE_APP_ID


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

WSGI_APPLICATION = 'insmart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
