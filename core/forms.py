"""
Core app forms for StartMarket.
"""

from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Contact form with CSRF protection and validation."""

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'company', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-transparent border-b border-gray-300 py-3 text-black placeholder-gray-400 focus:outline-none focus:border-black transition-colors duration-300',
                'placeholder': 'Your Name *',
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-transparent border-b border-gray-300 py-3 text-black placeholder-gray-400 focus:outline-none focus:border-black transition-colors duration-300',
                'placeholder': 'Your Email *',
                'autocomplete': 'email',
            }),
            'company': forms.TextInput(attrs={
                'class': 'w-full bg-transparent border-b border-gray-300 py-3 text-black placeholder-gray-400 focus:outline-none focus:border-black transition-colors duration-300',
                'placeholder': 'Company / Startup Name',
                'autocomplete': 'organization',
            }),
            'service': forms.Select(attrs={
                'class': 'w-full bg-transparent border-b border-gray-300 py-3 text-black focus:outline-none focus:border-black transition-colors duration-300 cursor-pointer appearance-none',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full bg-transparent border-b border-gray-300 py-3 text-black placeholder-gray-400 focus:outline-none focus:border-black transition-colors duration-300 resize-none',
                'placeholder': 'Tell us about your project *',
                'rows': 4,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Please enter a valid name.")
        return name

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise forms.ValidationError("Please provide more detail about your project.")
        return message
