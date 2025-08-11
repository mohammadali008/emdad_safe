
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from services.models import Service
from django.contrib.auth.models import User

class ServiceTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')
        self.service_data = {
            "title": "Test Service",
            "description": "This is a test service.",
            "tags": ["test", "demo"]
        }
        self.list_url = reverse("services_api:service-list")

    def test_create_service_as_admin(self):
        response = self.client.post(self.list_url, self.service_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)

    def test_list_services_as_anonymous(self):
        self.client.logout()
        Service.objects.create(title="S1", description="D1", is_active=True)
        Service.objects.create(title="S2", description="D2", is_active=False)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # فقط is_active=True

    def test_soft_delete(self):
        response = self.client.post(self.list_url, self.service_data, format='json')
        service_id = response.data['id']
        delete_url = reverse("services_api:service-detail", args=[service_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Service.objects.get(id=service_id).is_active)
