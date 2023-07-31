from django.shortcuts import render
from .models import FoodItem, DrinkItem


def menu(request):
    food_items = FoodItem.objects.all()
    drink_items = DrinkItem.objects.all()
    context = {
        'food_items': food_items,
        'drink_items': drink_items,
    }
    return render(request, 'menu.html', context)
