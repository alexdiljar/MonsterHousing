from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from User.models import Profile
from Properties.models import Cities, Addresses
from User.forms.profile_form import *

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'User/SignUp.html', {
        'form': UserCreationForm()
    })


def profile(request):
    auth_user = User.objects.filter(username=request.user)
    profile = Profile.objects.filter(user_id=User.objects.filter(username=request.user).first().id).first()
    addresses = Addresses.objects.filter(id=profile.address_id).first()
    cities = Cities.objects.filter(id=addresses.Cities_id).first()
    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        addresses_form = AddressesForm(instance=addresses, data=request.POST)
        cities_form = CitiesForm(instance=cities, data=request.POST)
        if profile_form.is_valid() and addresses_form.is_valid() and cities_form.is_valid():
            # We save information to db for cities
            cities.save()
            # We access db and id from prev saved data
            # We save information to db for addresses
            addresses = addresses_form.save(commit=False)
            addresses.Cities = cities
            addresses.save()
            # We access db and user and address from prev saved data
            # We save information to db for profile
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.address = addresses
            profile.save()
            return redirect('profile')
    return render(request, 'User/Account.html', {

        # TODO: need to add form for auth user so we can know first, last name and email

        'auth_user_form': AuthUserForm(instance=auth_user),
        'profile_form': ProfileForm(instance=profile),
        'addresses_form': AddressesForm(instance=addresses),
        'cities_form': CitiesForm(instance=cities)
    })


