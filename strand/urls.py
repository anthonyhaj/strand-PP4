from django.contrib import admin
from django.urls import path, include
from bookings import views as bookings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('home/', include('home.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
    path('', include('contact.urls')),
    path('login_required/', bookings_views.login_required_view, name='login_required'),
]
