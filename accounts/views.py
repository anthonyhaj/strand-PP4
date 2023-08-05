# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
# Internal
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def register(request):
    """
    Register new user. Handles user registration using the RegisterForm.
    """
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
    """
    Renders a success page after a user has successfully registered.
    """
    return render(request, 'success.html')


def login_view(request):
    """
    User login view. Handles user authentication and login.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'accounts/login.html')


def logout_confirm(request):
    """
    Logout confirmation view. Logs out the user when the
    confirmation form is submitted
    """
    if request.method == "POST":
        logout(request)
        return redirect('accounts:logout_confirmed')
    return render(request, 'logout_confirm.html')


def logout_confirmed(request):
    """
    Logout confirmation success view. Renders a page confirming
    the successful logout
    """
    return render(request, 'accounts/logout_confirmed.html')
