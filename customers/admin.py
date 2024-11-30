from django.contrib import admin
from .models import ServiceRequest

# Customizing the admin interface for ServiceRequest
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'request_type', 'status', 'created_at', 'updated_at')  # Columns to display in the list
    list_filter = ('status', 'request_type')  # Filter options for the admin panel
    search_fields = ('customer__username', 'request_type', 'status')  # Search fields
    date_hierarchy = 'created_at'  # Display a date hierarchy for filtering requests by date
    ordering = ('-created_at',)  # Default ordering (newest first)

# Register the ServiceRequest model with the admin interface
admin.site.register(ServiceRequest, ServiceRequestAdmin)
