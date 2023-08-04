from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('bookings:booking_confirmation') 
    else:
        form = BookingForm()
    return render(request, 'bookings.html', {'form': form})


def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')


def login_required_view(request):
    return render(request, 'login_required.html')

def mybookings(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(guest=request.user)
        return render(request, 'bookings/mybookings.html', {'bookings': bookings})
    else:
        return redirect('accounts:login')

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.guest:
        return redirect('accounts:login')

    if request.method == "POST":
        booking.delete()
        return redirect('bookings:mybookings')
    else:
        return render(request, 'bookings/confirm_delete.html', {'booking': booking})

@login_required
def change_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.guest:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings:mybookings') 
    else:
        form = BookingForm(instance=booking)
    return render(request, 'bookings/change_booking.html', {'form': form, 'booking': booking})
