from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/success/', views.register_success, name='success'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_confirm, name='logout'),
    path('logout/confirmed/', views.logout_confirmed, name='logout_confirmed'),
]
