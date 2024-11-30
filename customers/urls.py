from django.urls import path
from . import views

app_name = 'customers'  # Namespace for this app's URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.create_request, name='create_request'),
    #path('track-requests/', views.track_requests, name='track_requests'),
]
