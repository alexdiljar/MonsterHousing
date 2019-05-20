from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from Transactions.models import CreditCard, Transactions
from User.models import Profile


class UserInformationForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['id', 'phone', 'profile_image', 'address', 'user']
        fields = [
            'ssn'
        ]
        widgets = {
            'ssn': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Social Security Number'})
        }


class \
        PaymentForm(ModelForm):
    class Meta:
        model = CreditCard
        exclude = ['id', 'user']
        fields = [
            'cc_number',
            'cc_month',
            'cc_year',
            'cc_code'
        ]
        widgets = {
            'cc_number': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '0000-0000-0000-0000'}),
            'cc_month': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM'}),
            'cc_year': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'YY'}),
            'cc_code': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'cvv'})
        }


class TransactionForm(ModelForm):
    class Meta:
        model = Transactions
        exclude = ['id', 'transaction_date', 'property', 'buyer']
