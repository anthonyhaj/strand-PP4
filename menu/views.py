from django.shortcuts import render
from .models import FoodItem, DrinkItem, FOOD_TYPES, DRINK_TYPES


def menu(request):
    appetizers = FoodItem.objects.filter(type=1)
    main_courses = FoodItem.objects.filter(type=2)
    desserts = FoodItem.objects.filter(type=3)

    soft_drinks = DrinkItem.objects.filter(type=1)
    wines = DrinkItem.objects.filter(type=2)
    beers = DrinkItem.objects.filter(type=3)

    context = {
        'appetizers': appetizers,
        'main_courses': main_courses,
        'desserts': desserts,
        'soft_drinks': soft_drinks,
        'wines': wines,
        'beers': beers,
    }
    return render(request, 'menu.html', context)
