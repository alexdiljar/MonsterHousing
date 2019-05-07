from django.shortcuts import render

# Create your views here.


def about_us_index(request):
    return render(request, 'base/AboutUs.html')


def catalog_index(request):
    return render(request, 'base/Catalog.html')


def terms_index(request):
    return render(request, 'base/TermsAndConditions.html')


def front_page_index(request):
    return render(request, 'base/FrontPage.html.html')