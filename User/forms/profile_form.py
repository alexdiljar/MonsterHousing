from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses
from django.contrib.auth.models import User


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


class AuthUserForm(ModelForm):
    class Meta:
        model = User
        exclude = ['id', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'password': widgets.HiddenInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'})
        }

        # max_length=200,
        # null=True,
        # blank=True,
        # help_text='Use puns liberally',