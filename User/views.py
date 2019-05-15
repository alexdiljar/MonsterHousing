from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from User.models import Profile
from Properties.models import Addresses, Cities
from django.shortcuts import render, redirect, reverse, get_object_or_404
from User.forms.profile_form import CustomUserChangeForm, ProfileForm, AddressesForm, CitiesForm, RegisterForm


# Create your views here.
#def register(request):
    # registerin user for the first time, username and password

#    if request.method == "POST":
#        form = RegisterForm(data=request.POST)
#        if form.is_valid():
#            user_saved = form.save()
#            return redirect('register2')
#    return render(request, 'User/SignUp.html', {
#        'form': RegisterForm()
#    })

def register(request):
    if request.method == "POST":
        data = request.POST.copy()
        form = RegisterForm(data=request.POST)
        cities_form = CitiesForm(data=request.POST)
        addresses_form = AddressesForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if cities_form.is_valid() and addresses_form.is_valid() and profile_form.is_valid and form.is_valid():

            form_saved = form.save()
            city_saved = cities_form.save()
            address_saved = addresses_form.save(commit=False)
            profile_saved = profile_form.save(commit=False)

            address_saved.city = city_saved
            addresses_form.save()

            profile_saved.address = address_saved
            profile_saved.user = form_saved
            print(data)
            print()
            # profile_saved.user =
            profile_saved.save()

            return HttpResponseRedirect('login')
        else:
            request.method = "GET"
            pass
    if request.method == "GET":
        return render(request, 'User/SignUp.html', {
            'form': RegisterForm(),
            'cities_form': CitiesForm(),
            'addresses_form': AddressesForm(),
            'profile_form': ProfileForm(),
        })

'''return render(request, 'User/Account.html', {
    'user_form': CustomUserChangeForm(instance=user),
    'cities_form': CitiesForm(instance=profile.address.city),
    'addresses_form': AddressesForm(instance=profile.address),
    'profile_form': ProfileForm(instance=profile),
})
'''


def profile(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        # User has some saved information and need to update them
        # Step 1: Parse data from POST.
        user_form = CustomUserChangeForm(instance=user, data=request.POST)

        cities_form = CitiesForm(instance=Cities.objects.get_or_create(), data=request.POST)

        addresses_form = AddressesForm(instance=Addresses.objects.get_or_create(city=request.user.profile.address.city),
                                       data=request.POST)

        profile_form = ProfileForm(instance=Profile.objects.get_or_create(user=request.user,
                                   address=request.user.profile.address), data=request.POST)

        # Step 2: Validate parsed data.
        if user_form.is_valid() and cities_form.is_valid() and addresses_form.is_valid() and profile_form.is_valid():
            user_form.save()
            cities_form.save()
            addresses_form.save()
            profile_form.save()

            return redirect(reverse('profile'))
        # Validation failed - return same data parsed from POST.
        else:
            return render(request, 'User/Account.html', {
                'user_form': user_form,
                'cities_form': cities_form,
                'addresses_form': addresses_form,
                'profile_form': profile_form,

            })
    if request.method == "GET":
        # User has logged information and we want to GET all info
        if user.first_name != '':
            profile = Profile.objects.get(user=request.user)
            return render(request, 'User/Account.html', {
                'user_form': CustomUserChangeForm(instance=user),
                'cities_form': CitiesForm(instance=profile.address.city),
                'addresses_form': AddressesForm(instance=profile.address),
                'profile_form': ProfileForm(instance=profile),
            })


'''
def profile(request):
    cities = Cities.objects.first()
    addresses = Addresses.objects.filter(Cities=cities.id).first()
    profile = Profile.objects.filter(user=request.user, address=addresses.id).first()
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

        # 'auth_user_form': AuthUserForm(instance=auth_user)
        'profile_form': ProfileForm(instance=profile),
        'addresses_form': AddressesForm(instance=addresses),
        'cities_form': CitiesForm(instance=cities)
    })'''


def create_property(request):
    if request.method == "POST":
        data = request.POST.copy()
        type_form = TypeForm(data=request.POST)
        cities_form = CitiesForm(data=request.POST)
        addresses_form = AddressesForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if cities_form.is_valid() and addresses_form.is_valid() and profile_form.is_valid and form.is_valid():

            form_saved = form.save()
            city_saved = cities_form.save()
            address_saved = addresses_form.save(commit=False)
            profile_saved = profile_form.save(commit=False)

            address_saved.city = city_saved
            addresses_form.save()

            profile_saved.address = address_saved
            profile_saved.user = form_saved
            print(data)
            print()
            # profile_saved.user =
            profile_saved.save()

            return HttpResponseRedirect('login')
        else:
            request.method = "GET"
            pass
    if request.method == "GET":
        return render(request, 'User/SignUp.html', {
            'form': RegisterForm(),
            'cities_form': CitiesForm(),
            'addresses_form': AddressesForm(),
            'profile_form': ProfileForm(),
        })