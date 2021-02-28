import uuid

from django.db import models

from .validators import validate_pdf_file_extension


class PDFDocument(models.Model):
    document_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    date_uploaded = models.DateTimeField(auto_created=True)
    date_processed = models.DateTimeField(null=True, blank=True)

    original_document = models.ImageField(upload_to='pdf_document/%Y/%m/%d', validators=[validate_pdf_file_extension])

    @property
    def is_processed(self):
        return self.date_processed is not None

    @property
    def page_count(self):
        return len(self.pages)


class PDFPage(models.Model):
    document = models.ForeignKey('PDFDocument', related_name='pages', on_delete=models.CASCADE)
    page_number = models.IntegerField()
    page = models.ImageField(upload_to='pdf_page')
