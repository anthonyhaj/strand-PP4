# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Internal:
from .forms import BookingForm
from .models import Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@login_required
def book(request):
    """
    View to handle booking a restaurant table (requires login)
    """
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
    # View to display the booking confirmation page
    return render(request, 'bookings/booking_confirmation.html')


def login_required_view(request):
    # View to display a page indicating login is required.
    return render(request, 'login_required.html')


def mybookings(request):
    """
    View to display bookings for the authenticated user if logged in,
    otherwise redirects to login page.
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(guest=request.user)
        return render(request, 'bookings/mybookings.html', {
            'bookings': bookings})
    else:
        return redirect('accounts:login')


def delete_booking(request, booking_id):
    """
    View to delete a booking for the authenticated user
    If the booking exists and belongs to the user, it can be deleted.
    After successful deletion, the user sees success message
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.guest:
        return redirect('accounts:login')

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Your booking was successfully cancelled.")
        return redirect('bookings:mybookings')
    else:
        return render(request, 'bookings/confirm_delete.html', {
            'booking': booking})


@login_required
def change_booking(request, booking_id):
    """
    View to change/update a booking for the authenticated user
    If the form is valid, the booking information is updated, and the user is
    redirected to their bookings page.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.guest:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings:mybookings')
    else:
        initial_data = {
            'name': booking.name,
            'email': booking.email,
            'phone_number': booking.phone_number,
            'requested_date': booking.requested_date.strftime(
                "%Y-%m-%d") if booking.requested_date else None,
            'requested_time': booking.requested_time,
            'guest_count': booking.guest_count,
            'table': booking.table.id
        }
        form = BookingForm(instance=booking, initial=initial_data)

    return render(request, 'bookings/change_booking.html', {
        'form': form, 'booking': booking})
