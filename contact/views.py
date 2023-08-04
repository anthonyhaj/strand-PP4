from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/thank_you.html')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
