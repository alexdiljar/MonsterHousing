from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        exclude = ['id']
        widgets = {
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'zip': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.Select(attrs={'class': 'form-control'}),
        }


class AddressesForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['id', 'Cities_id']
        widgets = {
            'street': widgets.Select(attrs={'class': 'form-control'}),
            'house_no': widgets.Select(attrs={'class': 'form-control'}),
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
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
            'country': widgets.Select(attrs={'class': 'form-control'}),
            'zip': widgets.Select(attrs={'class': 'form-control'}),
            'city': widgets.Select(attrs={'class': 'form-control'}),
        }
