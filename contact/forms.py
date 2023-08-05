# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
# Internal:
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ContactForm(forms.ModelForm):
    """
    A ModelForm for the 'Contact' model.
    It defines the fields to be included in the form and
    customizes the 'message' field
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

    message = forms.CharField(widget=forms.Textarea, max_length=500)
