from django.urls import include, path
from rest_framework import routers

from .views import PDFPageViewSet, PDFDocumentViewSet

app_name = 'document'

router = routers.DefaultRouter()
router.register(r'document', PDFDocumentViewSet)
# router.register(r'document/<document_id>/page/<page_number>', PDFPageViewSet)

urlpatterns = [
    path('', include(router.urls))
]

