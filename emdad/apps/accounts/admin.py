from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('phone_number', 'is_active', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    ordering = ('phone_number',)
    search_fields = ('phone_number',)

    fieldsets = (
        (None, {'fields': ('phone_number',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ()}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number',),
        }),
    )
