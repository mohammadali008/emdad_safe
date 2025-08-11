from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'service', 'description', 'status', 'is_active', 'created_at']
        read_only_fields = ['user', 'created_at', 'is_active']
