from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.book, name='bookings'),
    path('mybookings/', views.mybookings, name='mybookings'),
]
