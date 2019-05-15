from typing import List

from django.forms import ModelForm, widgets
from django import forms
from Properties.models import *
from django_countries.fields import CountryField


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        exclude = ['id']
        country = CountryField()

        widgets = {
            'zip': widgets.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'city': widgets.TextInput(attrs={'class': 'form-control'})
        }


class AddressesForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['id', 'Cities']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_no': widgets.NumberInput(attrs={'class': 'form-control', 'min': 0})
        }


class TagsForm(ModelForm):
    class Meta:
        model = Tags
        exclude = ['id']
        widgets = {
            'elevator': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'garage': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'near_bloodbank': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'dungeon': widgets.CheckboxInput(attrs={'class': 'checkbox'}),
            'secret_entrance': widgets.CheckboxInput(attrs={'class': 'checkbox'})
        }


class TypesForm(ModelForm):
    class Meta:

        CHOICES = [(types.id, types.type) for types in Types.objects.all()]
        model = Types
        exclude = ['id']
        widgets = {
            'description': widgets.Select(attrs={'class': 'dropdown'}, choices=CHOICES)
        }


class DetailsForm(ModelForm):
    class Meta:
        model = Details
        exclude = ['id', 'T_ID', 'Ty_ID']
        widgets = {
            'size': widgets.TextInput(attrs={'class': 'form-control', 'min': 10}),
            'price': widgets.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'rooms': widgets.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'description': widgets.TextInput(attrs={'class': 'form-control'}),
            'property_image': widgets.URLInput(attrs={'class': 'form-control'})
        }


class PropertiesForm(ModelForm):
    class Meta:
        model = Properties
        exclude = ['id', 'address', 'detail', 'user', 'is_active']

class CreatePropertyForm:
    TagsForm(ModelForm)
    TypesForm(ModelForm)
    CitiesForm(ModelForm)
    AddressesForm(ModelForm)
    DetailsForm(ModelForm)
