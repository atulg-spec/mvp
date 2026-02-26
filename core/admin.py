"""
Admin configuration for the core app.
"""

from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'service', 'created_at', 'is_read')
    list_filter = ('service', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('name', 'email', 'company', 'service', 'message', 'created_at')
    list_per_page = 25

    def has_add_permission(self, request):
        return False
