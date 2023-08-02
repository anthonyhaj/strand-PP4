from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def book(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.guest = request.user
            booking.save()
            return redirect('home') 
    else:
        form = BookingForm()
    return render(request, 'bookings.html', {'form': form})

def login_required_view(request):
    return render(request, 'login_required.html')