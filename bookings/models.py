from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

class RestaurantTable(models.Model):
    name = models.CharField(max_length=50)
    max_seats = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'P', 'Pending'
        CONFIRMED = 'C', 'Confirmed'
        COMPLETED = 'CP', 'Completed'
        CANCELLED = 'CL', 'Cancelled'