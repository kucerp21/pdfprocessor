from PyPDF2 import PdfFileReader

from django.core.exceptions import ValidationError


def validate_pdf_file(value):
    try:
        PdfFileReader(value)
    except Exception:
        raise ValidationError('File is not a valid PDF')
