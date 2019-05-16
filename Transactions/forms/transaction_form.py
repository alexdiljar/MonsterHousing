from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses
from django import forms


class UserChangeFormPurchase(UserChangeForm):
    class Meta:
        model = User

        fields = [
            'last_name',
            'first_name',
            'email'
        ]

        widgets = {
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }