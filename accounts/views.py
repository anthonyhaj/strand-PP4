from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in to your account.')
            return redirect('accounts:success') 
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render(request, 'success.html')

