from django.shortcuts import render


# Create your views here.
def buy_property(request, id):
    return render(request, 'Transactions/Information.html')
