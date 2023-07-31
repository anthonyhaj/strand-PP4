from django.db import models

FOOD_TYPES = (
    (1, 'Appetizer'),
    (2, 'Main Course'),
    (3, 'Dessert'),
)

DRINK_TYPES = (
    (1, 'Soft Drink'),
    (2, 'Wine'),
    (3, 'Beer'),
)

class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.IntegerField(choices=FOOD_TYPES)

    def __str__(self):
        return self.name

class DrinkItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    type = models.IntegerField(choices=DRINK_TYPES)

    def __str__(self):
        return self.name
