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
    profile = Profile.objects.filter(user=request.user).first()
    addresses = Addresses.objects.filter(id=profile.address_id)
    cities = Cities.objects.filter(id=addresses.Cities_id)  # gæti þurft að vera stórir stafir í user
    if request.method == "POST":
        profile_form = ProfileForm(instance=profile, data=request.POST)
        addresses_form = AddressesForm(instance=addresses, data=request.POST)
        cities_form = CitiesForm(instance=cities, data=request.POST)

        if profile_form.is_valid() and addresses_form.is_valid() and cities_form.is_valid():
            cities = cities_form.save(commit=False)
            cities.save()
            addresses = addresses_form.save(commit=False)
            addresses.save()
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'User/Account.html', {
        'profile_form': ProfileForm(instance=profile),
        'addresses_form': AddressesForm(instance=addresses),
        'cities_form': CitiesForm(instance=cities)
    })
