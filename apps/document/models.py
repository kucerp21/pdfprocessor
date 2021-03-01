import uuid

from django.db import models

from .utils.validators import validate_pdf_file_extension


class PDFDocument(models.Model):

    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(null=True, blank=True)

    original_document = models.FileField(upload_to='pdf_document/%Y/%m/%d', validators=[validate_pdf_file_extension])

    @property
    def is_processed(self):
        return self.date_processed is not None

    @property
    def page_count(self):
        return self.pages.count()

    def get_status_display(self):
        if self.is_processed:
            return 'done'
        else:
            return 'processing'

    class Meta:
        verbose_name = "PDF Document"


class PDFPage(models.Model):
    document = models.ForeignKey('PDFDocument', related_name='pages', on_delete=models.CASCADE)
    page_number = models.IntegerField()
    page = models.ImageField(upload_to='pdf_page')

    class Meta:
        verbose_name = "PDF Page"
