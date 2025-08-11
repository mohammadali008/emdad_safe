from rest_framework import serializers
from .models import CustomUser, PhoneOTP
from django.utils import timezone


class PhoneLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        return value

    def create(self, validated_data):
        phone_number = validated_data["phone_number"]
        otp_entry = PhoneOTP.objects.create(phone_number=phone_number)
        # جای اتصال به سرویس پیامکی
        return otp_entry


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)

    def validate(self, data):
        phone_number = data["phone_number"]
        code = data["code"]

        try:
            otp_entry = PhoneOTP.objects.filter(phone_number=phone_number, code=code).latest("created_at")
        except PhoneOTP.DoesNotExist:
            raise serializers.ValidationError("Invalid code or phone number.")

        if otp_entry.is_expired():
            raise serializers.ValidationError("Verification code has expired.")
        if otp_entry.is_verified:
            raise serializers.ValidationError("Code already used.")

        data["otp_entry"] = otp_entry
        return data

    def create(self, validated_data):
        otp_entry = validated_data["otp_entry"]
        otp_entry.is_verified = True
        otp_entry.save()

        user, created = CustomUser.objects.get_or_create(phone_number=otp_entry.phone_number)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'phone_number', 'is_active', 'is_staff']
