from django import forms
from django.core.exceptions import ValidationError
from datetime import date, datetime, time
from .models import Booking, RestaurantTable, TimeSlots

class BookingForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    requested_date = forms.DateField(widget=forms.SelectDateWidget)
    requested_time = forms.ChoiceField(choices=TimeSlots.choices)
    guest_count = forms.IntegerField()
    table = forms.ModelChoiceField(queryset=RestaurantTable.objects.all())

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'requested_date', 'requested_time', 'guest_count', 'table']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['requested_time'].choice_field = True
        self.fields['table'].choice_field = True

    def clean(self):
        cleaned_data = super().clean()

        requested_date = cleaned_data.get('requested_date')
        requested_time = time.fromisoformat(cleaned_data.get('requested_time', ''))

        today = date.today()
        now = datetime.now().time()

        # Check if the requested date is today and the requested time has passed
        if requested_date == today and requested_time < now:
            raise ValidationError({
                'requested_time': ValidationError('The requested time is in the past.', code='past_time')
            })

        return cleaned_data
