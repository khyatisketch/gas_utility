from django.db import models
from django.contrib.auth.models import User

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ServiceRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('Repair', 'Repair'),
        ('Billing Issue', 'Billing Issue'),
        ('New Connection', 'New Connection'),
        ('Meter Reading', 'Meter Reading'),
        ('Other', 'Other')
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved')
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking to the User model (customer)
    request_type = models.CharField(max_length=100, choices=REQUEST_TYPE_CHOICES)
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request {self.id} - {self.customer.username} ({self.request_type})"
    
    def mark_as_resolved(self):
        """Helper function to mark the request as resolved."""
        self.status = 'Resolved'
        self.save()
    
    def time_taken_to_resolve(self):
        """Helper function to calculate the time taken to resolve the request."""
        if self.status == 'Resolved':
            return self.updated_at - self.created_at
        return None
