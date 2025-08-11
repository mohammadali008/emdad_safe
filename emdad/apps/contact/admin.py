from django.contrib import admin
from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_handled', 'created_at')
    list_filter = ('is_handled',)
    search_fields = ('name', 'phone_number', 'reason')
