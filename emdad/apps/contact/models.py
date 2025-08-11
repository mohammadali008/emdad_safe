from django.db import models

class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    reason = models.CharField(max_length=255, blank=True)
    is_handled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"
