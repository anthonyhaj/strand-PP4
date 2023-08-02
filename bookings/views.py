from django.shortcuts import render
from .forms import BookingForm

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
