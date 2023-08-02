from django import forms
from .models import Booking, RestaurantTable, TimeSlots

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['requested_date', 'requested_time', 'table', 'guest_count']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['table'].queryset = RestaurantTable.objects.filter(available=True)
        self.fields['requested_time'].choices = TimeSlots.choices
