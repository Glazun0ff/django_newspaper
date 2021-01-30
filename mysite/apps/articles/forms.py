from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import Comments


class CommentForm(forms.ModelForm):
    """Форма отзывов"""
    captcha = ReCaptchaField()

    class Meta:
        model = Comments
        fields = ('name', 'email', 'text', 'captcha')
        widgets = {
            'name': forms.TextInput(attrs={'id': 'contactusername', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'contactemail', "class": 'form-control'}),
            'text': forms.Textarea(attrs={'id': 'contactcomment', "class": 'form-control', 'rows': '4'})
        }
