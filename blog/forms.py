from django import forms
from .models import Comment
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox 

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'body', 'captcha']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 12}),
        }
