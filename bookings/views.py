from django.shortcuts import render, redirect
from .forms import BookingForm

def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.save()
            return redirect('bookings: my_bookings.html')
    else:
        form = BookingForm()

    return render(request, 'bookings/bookings.html', {'form': form})
