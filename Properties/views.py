from django.shortcuts import render
from django.http import HttpResponse

# TODO : connect views/ the urls to html files under User in this file


# Create your views here.
def properties(request):
    return HttpResponse('Hello from the properties views')


# /candies/[id]
def get_properties_by_id(request, id):

    # return render(request, 'Properties/User/Properties/PropertyDetails.html')
    pass
