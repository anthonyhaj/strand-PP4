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

    class TimeSlots(models.TextChoices):
        SLOT_1 = '12:00', '12:00 PM'
        SLOT_2 = '13:15', '1:15 PM'
        SLOT_3 = '14:30', '2:30 PM'
        SLOT_4 = '15:45', '3:45 PM'
        SLOT_5 = '17:00', '5:00 PM'
        SLOT_6 = '18:15', '6:15 PM'
        SLOT_7 = '19:30', '7:30 PM'
        SLOT_8 = '20:45', '8:45 PM'
        SLOT_9 = '22:00', '10:00 PM'
        SLOT_10 = '23:15', '11:15 PM'  
