# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
# Internal:
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@login_required
def contact(request):
    """
    View to handle the contact form submission and saving messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_received')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def message_received(request):
    """
    View to display a message indicating that the
    contact message has been received.
    """
    return render(request, 'contact/message_received.html')
