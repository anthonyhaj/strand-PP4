from django import forms
from .models import Booking, RestaurantTable, TimeSlots

class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    requested_date = forms.DateField(widget=forms.SelectDateWidget)
    requested_time = forms.ChoiceField(choices=TimeSlots.choices)
    requested_time.choice_field = True
    guests = forms.IntegerField()
    table = forms.ModelChoiceField(queryset=RestaurantTable.objects.all())
    table.choice_field = True

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'requested_date', 'requested_time', 'guests', 'table']
