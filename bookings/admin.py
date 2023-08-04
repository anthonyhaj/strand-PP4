from django.contrib import admin
from .models import Booking, RestaurantTable

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_guest_full_name', 'guest_count', 'status')

    def get_guest_full_name(self, obj):
        return f"{obj.guest.first_name} {obj.guest.last_name}"
    get_guest_full_name.short_description = 'Guest Name'  

admin.site.register(Booking, BookingAdmin)
admin.site.register(RestaurantTable)

