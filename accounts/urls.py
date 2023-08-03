from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/success/', views.register_success, name='success'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:logout_confirm'), name='logout'),
    path('logout/confirmed/', views.logout_confirmed, name='logout_confirmed'),
    path('logout_confirm/', views.logout_confirm, name='logout_confirm'), 
]
