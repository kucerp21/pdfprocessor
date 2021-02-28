import os
from django.core.exceptions import ValidationError


def validate_pdf_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extension = '.pdf'
    if not ext.lower() == valid_extension:
        raise ValidationError('Unsupported PDF file extension.')