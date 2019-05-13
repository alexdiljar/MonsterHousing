from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from Properties.models import Properties
from django.contrib.auth.decorators import login_required

# TODO : connect views/ the urls to html files under User in this file


# Create your views here.
def properties(request):
    return HttpResponse('Hello from the properties views')


def catalog_index(request):
    context = {'properties': Properties.objects.all()}
    return render(request, 'base/Catalog.html', context)


# /properties/[id]
def get_properties_by_id(request, id):
    return render(request, 'Properties/PropertyDetails.html', {
        'property': get_object_or_404(Properties, pk=id)
    })

@login_required
def get_seller_profile(request):
    return render(request, 'Properties/SellerDetails.html')


# This should maybe be in user views, not sure
def add_new_property(request):
    pass

def search_properties(request):
    pass