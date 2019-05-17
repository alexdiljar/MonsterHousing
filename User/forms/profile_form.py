from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses
from django_countries.fields import CountryField
from django import forms


class AddressesForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['id', 'city']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street'}),
            'house_no': widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'House Number'}),
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Security Number'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'profile_image': widgets.URLInput(attrs={'class': 'form-control', 'placeholder': 'Profile Image Url'}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User

        fields = [
            'last_name',
            'first_name',
            'email',
            'username',
        ]

        widgets = {
            'last_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'email': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
