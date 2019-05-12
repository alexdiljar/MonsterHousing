from django.contrib.auth.forms import UserCreationForm
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
    cities = Cities.objects.first()
    addresses = Addresses.objects.filter(Cities=cities.id).first()
    profile = Profile.objects.filter(user=request.user, address=addresses.id).first()
    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        addresses_form = AddressesForm(instance=addresses, data=request.POST)
        cities_form = CitiesForm(instance=cities, data=request.POST)

        if profile_form.is_valid() and addresses_form.is_valid() and cities_form.is_valid():
            # cities = cities_form.save(commit=False)
            cities.save()
            addresses = addresses_form.save(commit=False)
            addresses.Cities = cities
            addresses.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.address = addresses
            profile.save()
            return redirect('profile')
    return render(request, 'User/Account.html', {
        # 'auth_user_form': AuthUserForm(instance=auth_user)
        'profile_form': ProfileForm(instance=profile),
        'addresses_form': AddressesForm(instance=addresses),
        'cities_form': CitiesForm(instance=cities)
    })


