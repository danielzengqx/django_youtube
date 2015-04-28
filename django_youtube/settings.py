"""
Django settings for django_youtube project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4^^6(0r@m88gf35ko8yg)fk-$3^wm@5pje#2qnmp7i@@&0c**8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'joins',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_youtube.middleware.ReferMiddleware'
)

ROOT_URLCONF = 'django_youtube.urls'

WSGI_APPLICATION = 'django_youtube.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#SHARE_URL = "www.lauhchwithcode.com/?ref="
SHARE_URL = "127.0.0.1:80/?ref="

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
TEMPLATE_DIRS = {
        os.path.join(BASE_DIR, 'templates'),

    }

#Daniel: I think this is the reference for the {% static %}
STATIC_URL = '/main-static/'

#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
#STATICFILES_DIRS = (
#        os.path.join(BASE_DIR, 'static'),
#    )
#STATIC_ROOT = '/Users/daniel/daniel_code/project_mysite/django_youtube/static/static_root'
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
    #'/Users/daniel/daniel_code/project_mysite/django_youtube/static/static_dirs',
    #'/Users/daniel/daniel_code/project_mysite/django_youtube/static/static_root',
    )

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')
MEDIA_URL = '/media/'


print "here is BASE_DIR:"
print BASE_DIR

