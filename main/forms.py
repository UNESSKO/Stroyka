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
                'name': 'name',
                'type': 'text',
                'maxlength': '25',
                'placeholder': 'Ваше имя',
                'class': 'input-box',
                'id': "request_form_name"
            }),
            "phone": TextInput(attrs={
                'name': 'phone',
                'type': 'tel',
                'maxlength': '25',
                'placeholder': 'Телефон',
                'class': 'input-box',
                'id': 'request_form_phone'
            }),
            "email": TextInput(attrs={
                'name': 'email',
                'type': 'email',
                'maxlength': '40',
                'placeholder': 'Электронная почта',
                'class': 'input-box',
                'id': 'request_form_email'
            }),
            "comment": Textarea(attrs={
                'name': 'message',
                'maxlength': '25',
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
                'class': 'review-form-name',
                'id': 'review_form_name',
                'name': 'review-form-name',
                'type': 'text',
                'placeholder': 'Ваше имя'
            }),
            'company': TextInput(attrs={
                'class': "review-form-company",
                'id': "review_form_company",
                'name': "review-form-company",
                'type': "text",
                'placeholder': 'Ваша компания'
            }),
            'review': Textarea(attrs={
                'id': "review_form_textarea",
                'name': "review-form-review",
                'maxlength': '250',
                'placeholder': 'Ваш отзыв'
            })
        }
