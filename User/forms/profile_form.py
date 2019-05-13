from typing import List
import django
from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses
from django import forms


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        exclude = ['id']
        choices = ('USA', 'Romania', 'Iceland', 'Chile')
        widgets = {
            'country': widgets.(attrs={'class': 'form-control'},widget=forms.Select, choices=choices),
            'zip': widgets.NumberInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class AddressesForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['id', 'Cities_id']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_no': widgets.NumberInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(ModelForm):
    CitiesForm(ModelForm)
    AddressesForm(ModelForm)

    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'})
        }
