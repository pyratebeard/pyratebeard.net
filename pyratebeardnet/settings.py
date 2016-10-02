"""
django settings for pyratebeard.net

"""

import os

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/pyratebeardnet.key') as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

ADMINS = (
    ('pyratebeard', 'root@pyratebeard.net'),
)
MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

# database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'database/db.sqlite3'),
    }
}

# application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'root',
    'log',
    'mcc',
    'powerzone'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pyratebeardnet.urls'

WSGI_APPLICATION = 'pyratebeardnet.wsgi.application'

# static files (CSS, JavaScript, Images)

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# template stuff
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)
