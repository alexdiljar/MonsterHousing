from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from Properties.forms.properties_form import *
from Search.forms.search_form import SearchForm, SearchHistoryForm
from Properties.filters import PropertiesFilter


# TODO : connect views/ the urls to html files under User in this file


# Create your views here.
def properties(request):
    return HttpResponse('Hello from the properties views')

def catalog_index(request):

    if request.method == "POST":
        form = SearchForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('search_results')
        else:
            request.method = "GET"
            pass

    if request.method == "GET":
        country = request.GET.get('country', '')
        zip = request.GET.get('zip', '')
        sort = request.GET.get('sort', '')

        if sort != 'address__street':
            sort = 'detail__price'
        else:
            sort = 'address__street'


        property_list = Properties.objects.order_by(sort).filter(Q(is_active=True))
        if country and zip:
            property_list = Properties.objects.filter(Q(is_active=True) & Q(address__city__country=country) & Q(address__city__zip=zip))
        elif country:
            property_list = Properties.objects.filter(Q(is_active=True) & Q(address__city__country=country))

        elif zip:
            property_list = Properties.objects.filter(Q(is_active=True) & Q(address__city__zip=zip))

        context = {'properties': property_list,
                   'form': SearchForm()}

        return render(request, 'base/Catalog.html', context)





# /properties/[id]
def get_property_by_id(request, id):
    if request.user.id is None:
        context = {
            'property': get_object_or_404(Properties, pk=id)
        }
    else:
        #search_form = SearchHistoryForm(data=request.GET)
        #if search_form.is_valid():
         #   search_form.save()
        context = {
            'property': get_object_or_404(Properties, pk=id),
            'user': User.objects.get(pk=request.user.id)
        }
    return render(request, 'Properties/PropertyDetails.html', context)


# /[property id]/seller_profile
@login_required
def get_seller_profile(request, id):
    seller = {'seller': (get_object_or_404(Properties, pk=id)).user,
              'properties': (Properties.objects.filter(user=(get_object_or_404(Properties, pk=id)).user))}
    return render(request, 'Properties/SellerDetails.html', seller)




def search_view(request):
    f = PropertiesFilter(request.GET, queryset=Properties.objects.all())
    return render(request, 'Properties/SearchBar.html', {'filter': f})
