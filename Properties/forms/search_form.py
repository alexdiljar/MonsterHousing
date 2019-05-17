import required as required

from Search.models import Search
from django.forms import ModelForm, widgets
from typing import List

from django import forms
from Properties.models import *
from django_countries.fields import CountryField

TYPE_CHOICES = [(types.id, types.type) for types in Types.objects.all()]

SIZE_CHOICES = (('[10, 49]', '10 - 49'),
                ('[50, 99]', '50 - 99'),
                ('[100, 199]', '100 - 199'),
                ('[200, 249]', '200 - 249'),
                ('[250, 499]', '250 - 499'),
                ('[500, 749]', '500 - 749'),
                ('[750, 1000]', '750 - 1000+'))

MAX_PRICE = (('NULL', 'any'),
             ('300', '$300'),
             ('400', '$400'),
             ('500', '$500'),
             ('600', '$600'),
             ('700', '$700'),
             ('800', '$800'),
             ('900', '$900'),
             ('1000', '$1000'),
             ('1500', '$1500'),
             ('2000', '$2000'),
             ('3000', '$3000'),
             ('4000', '$4000'),
             ('5000', '$5000'))

TAGS_CHOICES = (('elevator', 'Elevator'),
                ('garage', 'Garage'),
                ('near_bloodbank', 'Near Bloodbank'),
                ('dungeon', 'Dungeon'),
                ('secret_entrance', 'Secret Entrance'))




class SearchForm(ModelForm):
    country = CountryField(blank_label='Country').formfield(required=False)

    class Meta:
        model = Search
        exclude = ['id']
        widgets = {
            'zip': widgets.NumberInput(attrs={'min': 0, 'type': 'number'}),
            'type': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown'}, choices=TYPE_CHOICES),
            'rooms': widgets.NumberInput(attrs={'min': 0, 'type': 'number', 'default': 0}),
            'size': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown'}, choices=SIZE_CHOICES),
            'price': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown'}, choices=MAX_PRICE),
            'tags': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown'}, choices=TAGS_CHOICES),
            'sort': widgets.Select(attrs={'class': 'dropdown'}, choices=(('name', 'Name'),
                                                                                            ('price', 'Price'))),
            'search': widgets.Textarea(attrs={'class': 'form-control'})
        }

    def save(self, commit=True):
        #if self.rooms == '':
         #   self.rooms = 0
        if commit:

            # If committing, save the instance and the m2m data immediately.
            self.instance.save()

        return self.instance

    save.alters_data = True


