from django.shortcuts import render, redirect
from .models import ServiceRequest

def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'manage_requests.html', {'requests': requests})

    
