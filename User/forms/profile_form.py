from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses
from django import forms


class CitiesForm(ModelForm):
    class Meta:
        model = Cities
        exclude = ['id']
        widgets = {
            'country': widgets.TextInput(attrs={'class': 'form-right'}),
            'zip': widgets.TextInput(attrs={'class': 'form-left'}),
            'city': widgets.TextInput(attrs={'class': 'form-right'}),
        }


class AddressesForm(ModelForm):
    class Meta:
        model = Addresses
        exclude = ['id', 'city']
        widgets = {
            'street': widgets.TextInput(attrs={'class': 'form-right'}),
            'house_no': widgets.NumberInput(attrs={'class': 'form-left'}),
        }


class ProfileForm(ModelForm):
    country = widgets.TextInput(attrs={'class': 'form-right'})
    city = widgets.TextInput(attrs={'class': 'form-right'})
    zip = widgets.NumberInput(attrs={'class': 'form-right'})
    street = widgets.TextInput(attrs={'class': 'form-right'})
    house_no = widgets.NumberInput(attrs={'class': 'form-right'})

    class Meta:
        model = Profile
        exclude = ['id', 'user', 'address']
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-left'}),
            'phone': widgets.TextInput(attrs={'class': 'form-right'}),
            'profile_image': widgets.URLInput(attrs={'class': 'form-left'}),
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
            'last_name': widgets.TextInput(attrs={}),
            'first_name': widgets.TextInput(attrs={}),
            'email': widgets.TextInput(attrs={}),
            'username': widgets.TextInput(attrs={}),
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
