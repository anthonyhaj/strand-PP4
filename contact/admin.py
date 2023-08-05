# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
# Internal:
from .models import Contact
from django.contrib import admin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model
    Allows searching by name and email
    """
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
