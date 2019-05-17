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


class Form(forms.Form):
    # Get all countries
    country = CountryField(blank_label='Country').formfield(
        required=False)

    zip = forms.CharField(label='Zip', max_length=5, required=False)

    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     required=False,
                                     choices=TYPE_CHOICES)
    # make rooms and size into slider
    rooms = forms.IntegerField(min_value=1, label='Rooms', widget=forms.NumberInput(
        attrs={'size': '10'}), required=False, initial='Rooms')

    size = forms.ChoiceField(widget=forms.RadioSelect,
                             required=False,
                             choices=SIZE_CHOICES)

    max_price = forms.ChoiceField(widget=forms.RadioSelect,
                                  required=False,
                                  choices=MAX_PRICE)

    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     required=False,
                                     choices=TAGS_CHOICES)

    sort = forms.ChoiceField(widget=forms.RadioSelect,
                             required=False,
                             choices=(('name', 'Name'),
                                      ('price', 'Price')))

    # text = forms.TimeField(initial='<Street name> <house no>, <zip> <city>, <country> ', max_le)#forms.CharField(widget=forms.Textarea, required = False, initial='<Street name> <house no>, <zip> <city>, <country> ', max_length=10)


class SearchForm(ModelForm):
    country = CountryField(blank_label='Country').formfield(required=False)

    class Meta:
        model = Search
        exclude = ['id']
        #fields = ('zip', 'type', 'rooms', 'size', 'price', 'tags', 'sort', 'search')
        widgets = {required: False,
            'zip': widgets.NumberInput(attrs={'min': 0, 'required': False, 'type': 'number',}),
            'type': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown', 'required': 'false'}, choices=TYPE_CHOICES),
            'rooms': widgets.NumberInput(attrs={'min': 0, 'required': False, 'type': 'number',}),
            'size': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown', 'required': 'false'}, choices=SIZE_CHOICES),
            'price': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown', 'required': 'false'}, choices=MAX_PRICE),
            'tags': widgets.CheckboxSelectMultiple(attrs={'class': 'dropdown', 'required': 'false'}, choices=TAGS_CHOICES),
            'sort': widgets.Select(attrs={'class': 'dropdown', 'required': 'false'}, choices=(('name', 'Name'),
                                                                                            ('price', 'Price'))),
            'search': widgets.Textarea(attrs={'class': 'form-control', 'required': 'false'})
        }
