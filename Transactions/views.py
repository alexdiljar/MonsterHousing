from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.forms import forms
from Properties.forms.properties_form import TypesForm, TagsForm, DetailsForm, PropertiesForm
from User.models import Profile
from Properties.models import Properties, Addresses, Cities
from django.shortcuts import render, redirect, reverse, get_object_or_404
from User.forms.profile_form import CustomUserChangeForm, ProfileForm, AddressesForm, RegisterForm
from Transactions.forms.transaction_form import UserInformationForm, PaymentForm
from Properties.forms.properties_form import CitiesForm
from Transactions.models import CreditCard


# Create your views here.
# def user_information_purchase(request, id):
#     return render(request, 'Transactions/Information.html', {'user': get_object_or_404(User, pk=request.user.id)})


def user_information_purchase(request, id):
    # user = User.objects.get(pk=request.user.id)
    # properties = Properties.objects.get(pk=id)
    if request.method == 'POST':
        # User has some saved information and need to update them
        # Step 1: Parse data from POST.
        cities_form = CitiesForm(instance=Cities.objects.get(id=request.user.profile.address.city.id),
                                 data=request.POST)

        addresses_form = AddressesForm(instance=Addresses.objects.get(city=request.user.profile.address.city),
                                       data=request.POST)
        payment_form = PaymentForm(data=request.POST)

    # Step 2: Validate parsed data.
    # print(payment_form.is_valid())
    # Payment form will never be valid, because we do not intend for this payment to go through
        if cities_form.is_valid() and addresses_form.is_valid() and payment_form.is_valid():
            country_input = cities_form.cleaned_data['country']
            cities_saved = cities_form.save(commit=False)
            cities_saved.country = country_input

            # user_form.save()
            cities_saved.save()

            addresses_saved = addresses_form.save(commit=False)
            addresses_saved.city = cities_saved
            addresses_saved.save()
            cc_number_input = payment_form.cleaned_data['cc_number']
            cc_month_input = payment_form.cleaned_data['cc_month']
            cc_year_input = payment_form.cleaned_data['cc_year']
            cc_code_input = payment_form.cleaned_data['cc_code']
            payment_form.save()

            return HttpResponseRedirect('review_purchase')
        # Validation failed - return same data parsed from POST.
        else:
            pass

    if request.method == "GET":
        # User has logged information and we want to GET all info
        profile = Profile.objects.get(user=request.user)
        return render(request, 'Transactions/Information.html', {
            'cities_form': CitiesForm(instance=profile.address.city),
            'addresses_form': AddressesForm(instance=profile.address),
            'payment_form': PaymentForm()
        })


def review_purchase(request, p_id, ):
    print(id)

    return render(request, 'Transactions/Review.html', {
        'property': Properties.objects.get(pk=id),
    })


def confirm_purchase(request, id):
    pass
