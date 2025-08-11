from rest_framework import viewsets, permissions
from .models import ContactRequest
from .serializers import ContactRequestSerializer

class ContactRequestViewSet(viewsets.ModelViewSet):
    serializer_class = ContactRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ContactRequest.objects.all()
        return ContactRequest.objects.none()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


# --- Transferred from view_api.py ---

from rest_framework import viewsets
from rest_framework.response import Response

class ContactRequestViewSet(viewsets.ViewSet):
    def create(self, request):
        # Placeholder: handle contact form submission
        return Response({"message": "Contact request submitted."})
