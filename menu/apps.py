# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.apps import AppConfig
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class MenuConfig(AppConfig):
    """
    MenuConfig class for configuring the menu app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'menu'
