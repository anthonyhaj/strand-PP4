from django.contrib import admin
from .models import FoodItem, DrinkItem

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(DrinkItem)
