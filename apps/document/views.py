import logging

from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response

from .serializers.document import PDFPageSerializer, PDFDocumentSerializer, PDFDocumentNormalizationStateSerializer
from .models import PDFPage, PDFDocument
from worker.tasks import normalize_pdf

logger = logging.getLogger(__name__)


class PDFPageViewSet(viewsets.ViewSet):
    queryset = PDFPage.objects.all()
    serializer_class = PDFPageSerializer

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            'document__document_id': view_kwargs['document_id'],
            'page_num': view_kwargs['page_number']
        }
        return self.queryset.filter(**lookup_kwargs)

    # def list(self, request):
    #     pass


class PDFDocumentViewSet(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        doc_id = response.data['id']
        normalize_pdf.s(doc_id=doc_id).delay()
        logger.info(f'Document id {doc_id} normalization has STARTED')

        response.status_code = status.HTTP_202_ACCEPTED
        return response

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PDFDocumentNormalizationStateSerializer
        if self.action == 'create':
            return PDFDocumentSerializer
