from .models import Application, Review
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from captcha.fields import ReCaptchaField


class ApplicationForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Application
        fields = ['name', 'phone', 'email', 'comment', 'captcha']

        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'input-box',
                'id': "request_form_name"
            }),
            "phone": TextInput(attrs={
                'placeholder': 'Телефон',
                'class': 'input-box',
                'id': 'request_form_phone'
            }),
            "email": TextInput(attrs={
                'placeholder': 'Электронная почта',
                'class': 'input-box',
                'id': 'request_form_email'
            }),
            "comment": Textarea(attrs={
                'class': 'message-box',
                'placeholder': 'Ваш запрос',
                'id': 'request_form_message'
            }),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'company', 'review']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Ваше имя'
            }),
            'company': TextInput(attrs={
                'placeholder': 'Ваша компания'
            }),
            'review': Textarea(attrs={
                'placeholder': 'Ваш отзыв'
            })
        }
