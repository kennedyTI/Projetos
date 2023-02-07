from django import forms
from django.contrib.auth import forms

# Nosso Código.
from .models import Users


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Users


class UserCreationsForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Users

        pass
