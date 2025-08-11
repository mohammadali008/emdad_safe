from django.db import models
from django.conf import settings
from apps.services.models import Service

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.title} - {self.user.phone_number}"



class TicketNotification(models.Model):
    ticket = models.ForeignKey("tickets.Ticket", on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sent_to_sms = models.BooleanField(default=False)
    is_seen_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for ticket #{self.ticket.id} - seen: {self.is_seen_by_admin}"
