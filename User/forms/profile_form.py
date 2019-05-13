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
    country = widgets.TextInput(attrs={'class': 'form-control'})
    city = widgets.TextInput(attrs={'class': 'form-control'})
    zip = widgets.TextInput(attrs={'class': 'form-control'})
    street = widgets.TextInput(attrs={'class': 'form-control'})
    house_no = widgets.TextInput(attrs={'class': 'form-control'})
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
        pass

        # max_length=200,
        # null=True,
        # blank=True,
        # help_text='Use puns liberally',