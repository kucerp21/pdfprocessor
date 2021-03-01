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


class PDFDocumentNormalizationStateSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)
    n_pages = serializers.IntegerField(read_only=True, source='page_count')

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = PDFDocument
        fields = ['status', 'n_pages']

class PDFPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFPage
        fields = ['document', 'page_number', 'page']
        read_only_fields = ['document', 'page_number', 'page']
