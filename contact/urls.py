from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('message_received/', views.message_received, name='message_received'),
]
