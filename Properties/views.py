from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from Properties.models import *
from django.contrib.auth.decorators import login_required
from Properties.forms.properties_form import *
# from Properties.forms.search_form import SearchForm


# TODO : connect views/ the urls to html files under User in this file


# Create your views here.
def properties(request):
    return HttpResponse('Hello from the properties views')


def catalog_index(request):
    context = {'properties': Properties.objects.all()}
    return render(request, 'base/Catalog.html', context)


# /properties/[id]
def get_property_by_id(request, id):
    return render(request, 'Properties/PropertyDetails.html', {
        'property': get_object_or_404(Properties, pk=id)
    })


# /[property id]/seller_profile
@login_required
def get_seller_profile(request, id):
    seller = {'seller': (get_object_or_404(Properties, pk=id)).user,
              'properties': (Properties.objects.filter(user=(get_object_or_404(Properties, pk=id)).user))}
    return render(request, 'Properties/SellerDetails.html', seller)


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            country_input = form.cleaned_data['Country']
            zip_input = form.cleaned_data['zip']
            # Type is multi select will be returned as list must iterate when comparing
            type_input_list = form.cleaned_data['type']
            size_input = form.cleaned_data['size']
            max_price_input = form.cleaned_data['max_price']
            tags_input = form.cleaned_data['tags']
            sort_input = form.cleaned_data['sort']

            print(country_input, str(zip_input), type_input_list, size_input, max_price_input, tags_input, sort_input)
            for prop in Properties.objects.all():
                type = prop.detail.type_id
                for type_input in type_input_list:

                    if int(type_input) == int(type):
                        print(prop)

    form = SearchForm()

    return render(request, 'Properties/SearchBar.html', {'form': form})
