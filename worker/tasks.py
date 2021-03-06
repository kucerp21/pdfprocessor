import time
import datetime
import logging
from io import BytesIO
from pdf2image import convert_from_path

from django.db import transaction
from django.conf import settings
from django.core.files import File

from .worker import app
from apps.document.models import PDFDocument, PDFPage
from pdfprocessor.exceptions import NormalizationException


logger = logging.getLogger(__name__)


@app.task(bind=True, name='normalize_pdf')
@transaction.atomic()
def normalize_pdf_and_save_pages(self, doc_id: int) -> None:
    doc_object = PDFDocument.objects.get(id=doc_id)
    if not doc_object:
        logger.info(f'Document id {doc_id} not found')
        return

    # simulate normalizing delay
    if settings.DEBUG:
        time.sleep(10)

    try:
        normalize_pdf(doc_object)
    except Exception:
        doc_object.date_failed = datetime.datetime.now()
        doc_object.save()
        logger.error(f'Document id {doc_id} normalization has FAILED')
        raise NormalizationException()

    doc_object.date_processed = datetime.datetime.now()
    doc_object.save()
    logger.info(f'Document id {doc_id} normalization has FINISHED')


def normalize_pdf(document: PDFDocument) -> None:
    pages = convert_from_path(document.original_document.path)
    for count, page in enumerate(pages):
        page.thumbnail(PDFPage.NORMALIZED_SIZE)
        # convert to savable PNG
        blob = BytesIO()
        page.save(blob, 'PNG')

        page_obj = PDFPage(document=document, page_number=count+1)
        page_obj.page.save(f'{page_obj.document.id}_{page_obj.page_number}.png', File(blob))
