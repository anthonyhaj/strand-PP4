from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/success/', views.register_success, name='success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

