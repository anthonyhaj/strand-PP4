from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in to your account.')
            return redirect('accounts:success') 
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def register_success(request):
    return render(request, 'success.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def logout_confirm(request):
    return render(request, 'accounts/logout_confirm.html')


