import logging

from rest_framework.decorators import action
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse

from .serializers.document import PDFDocumentSerializer, PDFDocumentNormalizationStateSerializer, PDFPageSerializer
from .models import PDFPage, PDFDocument
from worker.tasks import normalize_pdf

logger = logging.getLogger(__name__)


class PDFDocumentViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
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
        if self.action == 'pages':
            return PDFPageSerializer

    @action(methods=['get'], detail=True, url_path=r'pages/(?P<page_num>\d+)', url_name='pages')
    def pages(self, request, pk=None, page_num=None):
        instance = self.get_object()

        image_file = instance.page.open()
        response = HttpResponse(image_file, content_type='image/png')
        response['Content-Length'] = instance.page.size
        response['Content-Disposition'] = f'attachment; filename={instance.page.name}'

        return response

    def get_object(self):
        if self.action == 'pages':
            doc_id = self.kwargs.get('pk')
            page_num = self.kwargs.get('page_num')
            return PDFPage.objects.get(document=doc_id, page_number=page_num)
        else:
            return super().get_object()



