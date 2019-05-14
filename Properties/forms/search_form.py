from Properties.models import Properties
from django import forms
from django.forms import ModelForm, widgets
from django_countries.fields import CountryField

TYPE_CHOISES = (('Appartment', 'Appartment'),
                ('Castle', 'Castle'),
                ('Loft', 'Loft'),
                ('Mansion', 'Mansion'),
                ('Beach House', 'Beach House'),
                ('Detached Home', 'Detached House'))


class SearchForm(forms.Form):
    # Get all countries
    country = CountryField(
        blank_label='Country').formfield()  # forms.ChoiceField(choices=[('iceland','Iceland'), ('usa','USA')])
    zip = forms.CharField(label='Zip', max_length=15)
    type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                     required=False,
                                     choices=TYPE_CHOISES,)

class CountryForm(ModelForm):
    class Meta:
        model = Properties..Cities
        exclude = ['id']
        widgets = {
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
        }
