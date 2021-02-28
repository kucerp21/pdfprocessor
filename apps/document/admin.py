from django.contrib import admin
from .models import PDFDocument, PDFPage


admin.site.register(PDFDocument)
admin.site.register(PDFPage)
