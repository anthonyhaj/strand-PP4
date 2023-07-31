from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),  # define the menu view
]
