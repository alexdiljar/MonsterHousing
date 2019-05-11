from django.shortcuts import render
from Properties.models import *

# Create your views here.


def about_us_index(request):
    return render(request, 'base/AboutUs.html')


# def catalog_index(request):
#     context = {'properties': Properties.objects.all()}
#     return render(request, 'base/Catalog.html', context)


def terms_index(request):
    return render(request, 'base/TermsAndConditions.html')


def front_page_index(request):
    return render(request, 'base/FrontPage.html')