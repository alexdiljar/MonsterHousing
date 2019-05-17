from django.http import HttpResponseRedirect
from django.shortcuts import render

from Search.forms.search_form import SearchForm
from Properties.models import *
from Search.models import Search






def search_history(request):
    return render(request, 'User/AccountSearches.html', {
        'user': User.objects.get(pk=request.user.id),
        'properties': Properties.objects.filter(user=request.user).filter(is_active=True)
    })


