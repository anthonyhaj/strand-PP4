from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone



class RestaurantTable(models.Model):
    name = models.CharField(max_length=50)
    max_seats = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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


class Booking(models.Model):
    class BookingStatus(models.TextChoices):
        PENDING = 'PN', 'Pending'
        CONFIRMED = 'CF', 'Confirmed'
        COMPLETED = 'CM', 'Completed'
        CANCELLED = 'CL', 'Cancelled'
    
    created_date = models.DateTimeField(default=timezone.now)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=5, 
        choices=TimeSlots.choices,
        default=TimeSlots.SLOT_1,
    )
    table = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    seats = models.IntegerField()
    guest_count = models.IntegerField()
    status = models.CharField(
        max_length=2,
        choices=BookingStatus.choices,
        default=BookingStatus.PENDING,
    )

    def __str__(self):
        return f'{self.table.name} - {self.guest.username}'


    def clean(self):
        # Ensure seats and guest_count are not negative
        if self.seats < 0 or self.guest_count < 0:
            raise ValidationError("Seats and guest count cannot be negative.")

        # Ensure guest_count does not exceed seats
        if self.guest_count > self.seats:
            raise ValidationError("Guest count cannot exceed number of seats.")

        # Ensure requested_date is not in the past
        if self.requested_date < timezone.now().date():
            raise ValidationError("Requested date cannot be in the past.")