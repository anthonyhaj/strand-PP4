from django import forms
from .models import Booking, RestaurantTable, TimeSlots
from django.contrib.auth.models import User

class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True) # This can be used to get the full name.
    email = forms.EmailField(required=True) # This can be used to get the email.
    phone_number = forms.CharField(max_length=15, required=True) # This can be used to get the phone number.
    requested_date = forms.DateField(widget=forms.SelectDateWidget, required=True) # This can be used to get the date.
    requested_time = forms.ChoiceField(choices=TimeSlots.choices, required=True) # This can be used to get the time slot.
    guests = forms.IntegerField(required=True) # This can be used to get the number of guests.

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'requested_date', 'requested_time', 'guests', 'table']
