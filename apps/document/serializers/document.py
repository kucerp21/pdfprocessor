from rest_framework import serializers
from rest_framework.reverse import reverse as rf_reverse

from ..models import PDFDocument, PDFPage


class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ['id', 'original_document']
        extra_kwargs = {
            'original_document': {'write_only': True}
        }


class PDFPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFPage
        fields = ['document', 'page_number', 'page']
        read_only_fields = ['document', 'page_number', 'page']
