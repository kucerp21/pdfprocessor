from celery import Celery
from django.conf import settings

app = Celery()
app.conf.update(settings.CELERY)
