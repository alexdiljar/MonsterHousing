from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Properties.forms.properties_form import *

# TODO : connect views/ the urls to html files under User in this file


# Create your views here.
def properties(request):
    return HttpResponse('Hello from the properties views')


def catalog_index(request):
    context = {'properties': Properties.objects.all()}
    return render(request, 'base/Catalog.html', context)


# /properties/[id]
def get_property_by_id(request, id):
    print('in get properties by id')
    return render(request, 'Properties/PropertyDetails.html', {
        'property': get_object_or_404(Properties, pk=id)
    })

# /[property id]/seller_profile
@login_required
def get_seller_profile(request, id):
    seller = {'seller': (get_object_or_404(Properties, pk=id)).user, 'properties': (Properties.objects.filter(user=(get_object_or_404(Properties, pk=id)).user)) }
    return render(request, 'Properties/SellerDetails.html', seller)


def create_property(request):
    if request.method == "POST":
        type_form = TypesForm(data=request.POST)
        cities_form = CitiesForm(data=request.POST)
        addresses_form = AddressesForm(data=request.POST)
        tags_form = TagsForm(data=request.POST)
        details_form = DetailsForm(data=request.POST)
        if cities_form.is_valid() and addresses_form.is_valid() and type_form.is_valid and tags_form.is_valid()\
                and details_form.is_valid():

            city_saved = cities_form.save()
            address_saved = addresses_form.save(commit=False)
            type_saved = type_form.save()
            tags_saved = tags_form.save()
            details_saved = details_form.save(commit=False)

            address_saved.city = city_saved
            addresses_form.save()

            details_saved.T_ID = tags_saved
            details_saved.Ty_ID = type_saved
            details_form.save()

            return HttpResponseRedirect('profile')
        else:
            request.method = "GET"
            pass
    if request.method == "GET":
        return render(request, 'Properties/CreateProperty.html', {
            'cities_form': CitiesForm(),
            'addresses_form': AddressesForm(),
            'type_form': TypesForm(),
            'details_form': DetailsForm(),
        })
