from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from User.models import Profile
from Properties.models import Cities, Addresses
from django import forms
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class UserChangeFormPurchase(UserChangeForm):
    class Meta:
        model = User

        fields = [
            'last_name',
            'first_name',
            'email'
        ]

        widgets = {
            'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.TextInput(attrs={'class': 'form-control'})
        }


class PaymentForm(forms.Form):
    credit_card_number = CardNumberField(label='Card Number'),
    expiration_date = CardExpiryField(label='Expiration Date'),
    cvv_code = SecurityCodeField(label='CVV/CVC')
