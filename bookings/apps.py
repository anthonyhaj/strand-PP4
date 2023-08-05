# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig
# Internal
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class BookingsConfig(AppConfig):
    """
    App configuration for the 'bookings' app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
