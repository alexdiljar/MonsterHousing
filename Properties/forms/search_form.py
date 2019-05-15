from Properties.models import Tags
from django import forms
from django.forms import ModelForm, widgets
from django_countries.fields import CountryField

TYPE_CHOICES = (('1', 'Apartment'),
                ('2', 'Castle'),
                ('3', 'Loft'),
                ('4', 'Mansion'),
                ('5', 'Beach House'),
                ('6', 'Detached House'),
                ('7', 'Attached House'))

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
                ('secret_entrence', 'Secret Entrence'))


class SearchForm(forms.Form):
    # Get all countries


    country = CountryField(blank_label='Country').formfield(
        required=True)  # forms.ChoiceField(choices=[('iceland','Iceland'), ('usa','USA')])
    zip = forms.CharField(label='Zip', max_length=15, required=False)
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     required=False,
                                     choices=TYPE_CHOICES)
    # make rooms and size into slider
    rooms = forms.IntegerField(min_value=1, widget=forms.NumberInput(
        attrs={'size': '10'}), required=False)
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
