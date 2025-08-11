
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from accounts.models import PhoneOTP, CustomUser
from django.utils import timezone
import time

class AuthOTPTests(APITestCase):

    def setUp(self):
        self.phone_number = "09121234567"
        self.send_code_url = reverse("send-code")
        self.verify_code_url = reverse("verify-code")

    def test_send_code_valid(self):
        response = self.client.post(self.send_code_url, {"phone_number": self.phone_number})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(PhoneOTP.objects.filter(phone_number=self.phone_number).exists())

    def test_send_code_invalid_number(self):
        response = self.client.post(self.send_code_url, {"phone_number": "invalid_number"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verify_correct_code(self):
        otp = PhoneOTP.objects.create(phone_number=self.phone_number)
        response = self.client.post(self.verify_code_url, {
            "phone_number": self.phone_number,
            "code": otp.code
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(CustomUser.objects.filter(phone_number=self.phone_number).exists())

    def test_verify_wrong_code(self):
        otp = PhoneOTP.objects.create(phone_number=self.phone_number)
        response = self.client.post(self.verify_code_url, {
            "phone_number": self.phone_number,
            "code": "000000"
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_verify_expired_code(self):
        otp = PhoneOTP.objects.create(phone_number=self.phone_number)
        otp.expires_at = timezone.now() - timezone.timedelta(minutes=1)
        otp.save()

        response = self.client.post(self.verify_code_url, {
            "phone_number": self.phone_number,
            "code": otp.code
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_verification(self):
        otp = PhoneOTP.objects.create(phone_number=self.phone_number)
        otp.is_verified = True
        otp.save()

        response = self.client.post(self.verify_code_url, {
            "phone_number": self.phone_number,
            "code": otp.code
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
