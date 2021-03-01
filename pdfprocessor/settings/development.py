from pdfprocessor.settings.base import *

SECRET_KEY = 'asd1v5tb16rv1wcwe6rv1ef6av51w5erv1v10csvfvc'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

DEBUG = True

ALLOWED_HOSTS += ['0.0.0.0']

INSTALLED_APPS += ['django_extensions']
