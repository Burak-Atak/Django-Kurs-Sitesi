from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    message = forms.CharField(max_length=1000, required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}))

    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'email', 'message']
