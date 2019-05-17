
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from User.models import Profile
from Properties.models import Properties, Addresses, Cities
from django.shortcuts import render
from User.forms.profile_form import AddressesForm
from Transactions.forms.transaction_form import UserInformationForm, PaymentForm, TransactionForm
from Properties.forms.properties_form import CitiesForm
from Transactions.models import CreditCard
from User.views import sell_property


# Create your views here.
# def user_information_purchase(request, id):
#     return render(request, 'Transactions/Information.html', {'user': get_object_or_404(User, pk=request.user.id)})


def user_information_purchase(request, id):
    delete_transaction(request)
    # user = User.objects.get(pk=request.user.id)
    # properties = Properties.objects.get(pk=id)
    if request.method == 'POST':
        # User has some saved information and need to update them
        # Step 1: Parse data from POST.
        cities_form = CitiesForm(instance=Cities.objects.get(id=request.user.profile.address.city.id),
                                 data=request.POST)

        addresses_form = AddressesForm(instance=Addresses.objects.get(city=request.user.profile.address.city),
                                       data=request.POST)
        user_form = UserInformationForm(instance=Profile.objects.get(user=request.user.id), data=request.POST)

        payment_form = PaymentForm(data=request.POST)

        # Step 2: Validate parsed data.
        # print(payment_form.is_valid())
        # Payment form will never be valid, because we do not intend for this payment to go through
        if cities_form.is_valid() and addresses_form.is_valid() and payment_form.is_valid() and user_form.is_valid():
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
            payment_saved = payment_form.save(commit=False)
            payment_saved.user = request.user
            payment_saved.save()
            user_form.save()
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
            'payment_form': PaymentForm(),
            'user_form': UserInformationForm(instance=profile)
        })


def review_purchase(request, id):
    if request.method == 'GET':
        return render(request, 'Transactions/Review.html', {
            'property': Properties.objects.get(pk=id),
            'user': User.objects.get(pk=request.user.id),
            'payment': CreditCard.objects.get(user=request.user)
        })
    if request.method == 'POST':
        return HttpResponseRedirect('confirm_purchase')


def confirm_purchase(request, id):
    if request.method == 'POST':
        transaction_form = TransactionForm(data=request.POST)
        if transaction_form.is_valid():
            transaction_saved = transaction_form.save(commit=False)
            transaction_saved.buyer = User.objects.get(pk=request.user.id)
            transaction_saved.property = Properties.objects.get(pk=id)
            transaction_saved.save()
            sell_property(request, id)
            delete_transaction(request)
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render(request, 'Transactions/Confirm.html', {
            'property': Properties.objects.get(pk=id)})


def delete_transaction(request):
    CreditCard.objects.all().delete()
    return
