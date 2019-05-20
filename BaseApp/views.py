from django.shortcuts import render
from Properties.models import Properties


# Create your views here.


def about_us_index(request):
    return render(request, 'base/AboutUs.html')


def terms_index(request):
    return render(request, 'base/TermsAndConditions.html')


def front_page_index(request):
    context = {'properties': Properties.objects.all()}
    return render(request, 'base/FrontPage.html', context)
