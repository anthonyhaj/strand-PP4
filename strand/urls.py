from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('home/', include('home.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
]
