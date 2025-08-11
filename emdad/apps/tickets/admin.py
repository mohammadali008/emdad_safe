from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'service', 'status', 'is_active', 'created_at')
    list_filter = ('status', 'is_active')
    search_fields = ('user__phone_number', 'service__title', 'description')



from .models import TicketNotification

@admin.register(TicketNotification)
class TicketNotificationAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'message', 'created_at', 'is_seen_by_admin', 'is_sent_to_sms']
    list_filter = ['is_seen_by_admin', 'is_sent_to_sms', 'created_at']
    search_fields = ['ticket__id', 'message', 'ticket__user__phone_number']
