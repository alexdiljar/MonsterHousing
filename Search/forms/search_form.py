from django.forms import ModelForm
from Search.models import Search
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


class SearchForm(forms.Form):
    # Only three fields that we slimmed the search down to
    country = CountryField(blank_label='Country').formfield(
        required=False)

    zip = forms.CharField(label='Zip', max_length=5, required=False)

    sort = forms.ChoiceField(widget=forms.RadioSelect,
                             required=False,
                             choices=(('address__street', 'Name'),
                                      ('detail__price', 'Price')))


class SearchHistoryForm(ModelForm):
    class Meta:
        model = Search
        exclude = ['id', 'user', 'property']



