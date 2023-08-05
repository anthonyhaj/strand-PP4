# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
# Internal
from .models import Booking, RestaurantTable
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BookingAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for Booking model
    """
    list_display = ('id', 'get_guest_full_name', 'guest_count', 'status')

    def get_guest_full_name(self, obj):
        """
        Returns the full name of the guest for the admin interface
        """
        return f"{obj.guest.first_name} {obj.guest.last_name}"
    get_guest_full_name.short_description = 'Guest Name'


admin.site.register(Booking, BookingAdmin)
admin.site.register(RestaurantTable)
