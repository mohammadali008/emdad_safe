
from rest_framework import viewsets, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = BlogPost.objects.filter(is_active=True)
        if self.request.user.is_staff:
            queryset = BlogPost.objects.all()
        tag = self.request.query_params.get("tag")
        if tag:
            queryset = queryset.filter(tags__name__in=[tag])
        return queryset

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
