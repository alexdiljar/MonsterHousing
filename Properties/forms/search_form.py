from Properties.models import Tags
from django import forms
from django.forms import ModelForm, widgets
from django_countries.fields import CountryField

TYPE_CHOICES = (('1', 'Appartment'),
                ('2', 'Castle'),
                ('3', 'Loft'),
                ('4', 'Mansion'),
                ('5', 'Beach House'),
                ('6', 'Detached House'))

SIZE_CHOICES = (('10 - 49', '10 - 49'),
                ('50 - 99', '50 - 99'),
                ('100 - 199', '100 - 199'),
                ('200 - 249', '200 - 249'),
                ('250 - 499', '250 - 499'),
                ('500 - 749', '500 - 749'),
                ('750 - 1000+', '750 - 1000+'))


class SearchForm(forms.Form):
    # Get all countries
    country = CountryField(
        blank_label='Country').formfield(
        required=False)  # forms.ChoiceField(choices=[('iceland','Iceland'), ('usa','USA')])
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
    #price =
    # other
    # sort
