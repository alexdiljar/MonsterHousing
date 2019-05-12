from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Properties.models import Properties

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
    # return render(request, 'Properties/User/Properties/PropertyView.html')
