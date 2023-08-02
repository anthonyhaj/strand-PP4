from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.book, name='bookings'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]
