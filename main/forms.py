from .models import Application
from django.forms import ModelForm


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'phone', 'email', 'comment']
