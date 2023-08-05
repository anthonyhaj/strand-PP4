
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
# Internal:
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Form for user registration
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # Meta class to define the model and fields used in the form
        model = User
        fields = ["username", "email", "password1", "password2"]
