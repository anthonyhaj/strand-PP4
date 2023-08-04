from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_received')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def message_received(request):
    return render(request, 'contact/message_received.html')
