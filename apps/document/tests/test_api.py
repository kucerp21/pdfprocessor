from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status


class DocumentTestCase(APITestCase):
    """
    These tests serve only as example, it is heavily suggested to extend them
    """
    def setUp(self):
        self.factory = APIRequestFactory()
        self.test_pdf_path = 'apps/document/tests/static_files/test.pdf'
        self.output_0_path = 'static_files/normalized_0.png'
        self.output_1_path = 'static_files/normalized_1.png'

    def test_get_invalid_document_id(self):
        url = reverse('document:pdfdocument-detail', args=['777'])
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_pdfdocument(self):
        url = reverse('document:pdfdocument-list')
        data = {
            "original_document": open(self.test_pdf_path, "rb"),
            "name": "test.pdf"
            }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)
        self.assertTrue(response.data['id'])
