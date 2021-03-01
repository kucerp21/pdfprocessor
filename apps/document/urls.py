from django.urls import include, path
from rest_framework import routers

from .views import PDFDocumentViewSet

app_name = 'document'

router = routers.DefaultRouter()
router.register(r'document', PDFDocumentViewSet)

urlpatterns = [
    path('', include(router.urls))
]

