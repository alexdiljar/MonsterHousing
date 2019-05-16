from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from Properties.forms.properties_form import TypesForm, TagsForm, DetailsForm, PropertiesForm
from User.models import Profile
from Properties.models import Properties, Addresses, Cities
from django.shortcuts import render, redirect, reverse, get_object_or_404
from User.forms.profile_form import CustomUserChangeForm, ProfileForm, AddressesForm, CitiesForm, RegisterForm
from Transactions.forms.transaction_form import UserChangeFormPurchase, PaymentForm


# # Create your views here.
# def user_information_purchase(request, id):
#     user = User.objects.get(pk=request.user.id)
#     if request.method == 'POST':
#         # User has some saved information and need to update them
#         # Step 1: Parse data from POST.
#         user_form = UserChangeFormPurchase(instance=user, data=request.POST)
#
#         cities_form = CitiesForm(instance=Cities.objects.get_or_create(request.user.profile.address.city
#                                                                        ), data=request.POST)
#
#         addresses_form = AddressesForm(instance=Addresses.objects.get_or_create(city=request.user.profile.address),
#                                        data=request.POST)
#
#         # Step 2: Validate parsed data.
#         if user_form.is_valid() and cities_form.is_valid() and addresses_form.is_valid():
#             user_form.save()
#             cities_form.save()
#             addresses_form.save()
#
#             return render(request, 'Transactions/Payment.html')
#         # Validation failed - return same data parsed from POST.
#         else:
#             return render(request, 'Transactions/Information.html', {
#                 'user_form': user_form,
#                 'cities_form': cities_form,
#                 'addresses_form': addresses_form,
#             })
#     if request.method == "GET":
#         # User has logged information and we want to GET all info
#         if user.first_name != '':
#             profile = Profile.objects.get(user=request.user)
#             return render(request, 'Transactions/Information.html', {
#                 'user_form': UserChangeFormPurchase(instance=user),
#                 'cities_form': CitiesForm(instance=profile.address.city),
#                 'addresses_form': AddressesForm(instance=profile.address)
#             })


#
def payment_information_purchase(request, id):
    if request.method == 'POST':
        payment_form: PaymentForm()
        if payment_form.is_valid():
            return render(request, 'Transactions/Review.html', {
                'payment_form': PaymentForm()
            })


def review_purchase(request, id):
    pass


def confirm_purchase(request, id):
    pass
