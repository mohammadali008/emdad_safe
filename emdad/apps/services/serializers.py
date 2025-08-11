from rest_framework import serializers
from .models import Service
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class ServiceSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'tags', 'is_active', 'created_at']
        read_only_fields = ['created_at']
