# forms.py
from django import forms
from .models import ContactMessage

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'document']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your email address'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 12, 
                'placeholder': 'Enter your message'
            }),
            'document': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'message': 'Message',
            'document': 'Attachment (optional)',
        }
        help_texts = {
            'document': 'Optional: Upload PDF, DOCX or relevant document.',
        }



