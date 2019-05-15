from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.buy_property, name='buy_property'),
]