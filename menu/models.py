# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Choices for food types
FOOD_TYPES = (
    (1, 'Appetizer'),
    (2, 'Main Course'),
    (3, 'Dessert'),
)

# Choices for drink types
DRINK_TYPES = (
    (1, 'Soft Drink'),
    (2, 'Wine'),
    (3, 'Beer'),
)


class FoodItem(models.Model):
    """
    Model to represent food items in the menu
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.IntegerField(choices=FOOD_TYPES)

    def __str__(self):
        return self.name


class DrinkItem(models.Model):
    """
    Model to represent drink items in the menu.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.IntegerField(choices=DRINK_TYPES)

    def __str__(self):
        return self.name
