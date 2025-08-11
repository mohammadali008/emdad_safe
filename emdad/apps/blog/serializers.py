
from rest_framework import serializers
from .models import BlogPost
from taggit.serializers import (TagListSerializerField, TaggitSerializer)

class BlogPostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'tags', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
