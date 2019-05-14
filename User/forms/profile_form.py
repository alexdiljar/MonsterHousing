from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        exclude = ['id']
        widgets = {
            'country': widgets.TextInput(attrs={'class': 'form-control'}),
            'zip': widgets.TextInput(attrs={'class': 'form-control'}),
            'city': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class AddressesForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['id', 'Cities']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control'}),
            'house_no': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
            'profile_image': widgets.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User

        fields = [
            'last_name',
            'first_name',
            'email',
        ]

        widgets = {
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'}),
        }

