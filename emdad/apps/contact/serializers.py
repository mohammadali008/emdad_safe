from rest_framework import serializers
from .models import ContactRequest

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = ['id', 'name', 'phone_number', 'reason', 'is_handled', 'created_at']
        read_only_fields = ['is_handled', 'created_at']
