import time
import datetime
import logging

from .worker import app
from apps.document.models import PDFDocument, PDFPage


logger = logging.getLogger(__name__)


@app.task(bind=True, name='normalize_pdf')
def normalize_pdf(self, doc_id):
    doc_object = PDFDocument.objects.get(id=doc_id)
    if not doc_object:
        logger.info(f'Document id {doc_id} not found')
        return

    time.sleep(10)  # simulate normalizing

    doc_object.date_processed = datetime.datetime.now()
    doc_object.save()
    logger.info(f'Document id {doc_id} normalization has FINISHED')
