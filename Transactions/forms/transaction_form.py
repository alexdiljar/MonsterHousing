from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets

from User.models import Profile
from Properties.models import Cities, Addresses
from Transactions.models import CreditCard
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class UserInformationForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'ssn',
            'phone'
        ]
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control'}),
            'phone': widgets.TextInput(attrs={'class': 'form-control'}),
        }


class PaymentForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = [
            'cc_number',
            'cc_month',
            'cc_year',
            'cc_code'
        ]
        widgets = {
            'cc_number': widgets.TextInput(attrs={'class': 'form-control', 'title': '0000-0000-0000-0000'}),
            'cc_month': widgets.TextInput(attrs={'class':'form-control', 'title': 'MM'}),
            'cc_year': widgets.TextInput(attrs={'class':'form-control', 'title': 'YY'}),
            'cc_code': widgets.TextInput(attrs={'class': 'form-control', 'title':'cvv'})
        }
