
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from faq.models import FAQ
from django.contrib.auth.models import User

class FAQTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')
        self.faq_data = {
            "question": "What is this?",
            "answer": "This is a test FAQ."
        }
        self.list_url = reverse("faq_api:faq-list")

    def test_create_faq_as_admin(self):
        response = self.client.post(self.list_url, self.faq_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FAQ.objects.count(), 1)

    def test_list_faq_as_anonymous(self):
        self.client.logout()
        FAQ.objects.create(question="Q1", answer="A1", is_active=True)
        FAQ.objects.create(question="Q2", answer="A2", is_active=False)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_soft_delete_faq(self):
        response = self.client.post(self.list_url, self.faq_data, format='json')
        faq_id = response.data['id']
        delete_url = reverse("faq_api:faq-detail", args=[faq_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FAQ.objects.get(id=faq_id).is_active)
