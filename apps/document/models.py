from django.db import models
from django.core.validators import FileExtensionValidator


class PDFDocument(models.Model):

    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateTimeField(null=True, blank=True)
    date_failed = models.DateTimeField(null=True, blank=True)

    original_document = models.FileField(upload_to='pdf_document/%Y/%m/%d', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    @property
    def is_processed(self):
        return self.date_processed is not None

    @property
    def is_failed(self):
        return self.date_failed is not None

    @property
    def page_count(self):
        return self.pages.count()

    def get_status_display(self):
        if self.is_processed:
            return 'done'
        elif self.is_failed:
            return 'failed'
        else:
            return 'processing'

    class Meta:
        verbose_name = "PDF Document"


class PDFPage(models.Model):
    NORMALIZED_SIZE = 1200, 1600
    document = models.ForeignKey('PDFDocument', related_name='pages', on_delete=models.CASCADE)
    page_number = models.IntegerField()  # pages indexed from 1
    page = models.ImageField(upload_to='pdf_page')

    class Meta:
        verbose_name = "PDF Page"
