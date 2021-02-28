from rest_framework import viewsets, mixins, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from .serializers.document import PDFPageSerializer, PDFDocumentSerializer
from .models import PDFPage, PDFDocument


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


class PDFDocumentViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # TODO start async normalization

        response.status_code = status.HTTP_202_ACCEPTED
        return response
